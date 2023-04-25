import datetime
import os

import openai
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from technical_support.models import ChatMessage

channel_layer = get_channel_layer()


@shared_task
def create_response(session_id: str):
    messages_list = ChatMessage.objects.filter(session_id=session_id).values_list("text", "role")
    messages = [{"role": "assistant" if item[1] else "user", "content": item[0]} for item in messages_list]
    answer = openai.ChatCompletion.create(messages=messages, model="gpt-3.5-turbo")
    response_text = answer['choices'][0]["message"]["content"].strip()
    ChatMessage(role=True, text=response_text, time=datetime.datetime.now(), session_id=session_id).save()
    async_to_sync(channel_layer.group_send)(
        session_id, {"type": "send.answer", "text": response_text}
    )