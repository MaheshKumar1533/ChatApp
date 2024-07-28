from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message = models.TextField(max_length=100)
    Reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recieved_messages")
    message_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
