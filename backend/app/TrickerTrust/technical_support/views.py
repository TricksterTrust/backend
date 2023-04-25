import datetime
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from core.celery import app
from technical_support.models import ChatMessage


async def disconnect(consumer_instance: AsyncJsonWebsocketConsumer, _, session_id):
    await consumer_instance.send_json({"status": "disconnected", "description": "by request", "session_id": session_id},
                                      close=True)


async def get_history(consumer_instance: AsyncJsonWebsocketConsumer, _, session_id):
    messages_list = ChatMessage.objects.filter(session_id=session_id).values_list("text", "role", "time")
    messages = [{"role": item[1],
                 "content": item[0],
                 "time": item[2].strftime("%H:%M %Y-%m-%d")}
                for item in messages_list]
    await consumer_instance.send_json({"messages": messages, "session_id": session_id})


requests = {
    "history": get_history,
    "disconnect": disconnect
}


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def get_session(self):
        parsed_query_string = parse_qs(self.scope["query_string"])
        session_id = parsed_query_string.get(b"session_id")

        if session_id is None:
            return await self.send_json({"status": "disconnected",
                                         "description": "need session_id to use websocket"}, close=True)

        return parsed_query_string.get(b"session_id")[0].decode("utf-8")

    async def connect(self):
        await self.accept()
        session_id = await self.get_session()

        await self.channel_layer.group_add(session_id, self.channel_name)
        await self.send_json({"status": "connected", "session_id": session_id})

    async def receive_json(self, content, **kwargs):
        session_id = await self.get_session()

        if content.get("message") is None and content.get("request") is None:
            return await self.send_json({"status": "invalid message", "session_id": session_id})

        await self.send_json({"status": "accepted"})

        if content.get("request") and requests.get(content["request"]):
            return await requests[content["request"]](self, content, session_id)

        if content.get("message"):
            ChatMessage(text=content["message"], session_id=session_id, time=datetime.datetime.now(), role=False).save()
            app.send_task("technical_support.tasks.create_response", kwargs={
                "session_id": session_id
            })

    async def disconnect(self, code):
        session_id = await self.get_session()
        await self.channel_layer.group_discard(session_id, self.channel_name)

    async def send_answer(self, event):
        session_id = await self.get_session()
        await self.send_json({"answer": event["text"], "session_id": session_id})
