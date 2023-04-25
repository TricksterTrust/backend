from django.db import models


class ChatMessage(models.Model):
    text = models.CharField(max_length=8000)
    role = models.BooleanField(default=False)  # False - user, True - answer
    session_id = models.CharField(max_length=100)
    time = models.DateTimeField()
