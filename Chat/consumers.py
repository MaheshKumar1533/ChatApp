# Chat/consumers.py

import json, os, django
from channels.generic.websocket import WebsocketConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')
django.setup()


from Chat.models import Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    connected_clients = set()

    def connect(self):
        # Add this client to the set of connected clients
        ChatConsumer.connected_clients.add(self)
        self.accept()
        user = User.objects.get(username=self.scope["user"])
        for client in self.connected_clients:
            if client != self:
                reciepient = User.objects.get(username=client.scope["user"])
                client.send(text_data=json.dumps({
                    'type': 'connected',
                    'id': user.id,
                    'message': f'{user.username}',
                }))
                self.send(text_data=json.dumps({
                    'type': 'connected',
                    'id': reciepient.id,
                    'message': f'{client.scope["user"]}',
                }))
        print("Connected")

    def disconnect(self, code):
        # Remove this client from the set of connected clients
        ChatConsumer.connected_clients.remove(self)
        sender = User.objects.get(username=self.scope["user"])
        for client in self.connected_clients:
            receiver = User.objects.get(username=client.scope["user"].username)
            sent_messages = Message.objects.filter(Sender=sender, Reciever=receiver)
            received_messages = Message.objects.filter(Sender=receiver, Reciever=sender)
            all_messages = sent_messages | received_messages
            messages = all_messages.order_by('message_time').values()
            client.send(text_data=json.dumps({
                'type': 'disconnected',
                'id': sender.id,
                'message': f'{sender.username}',
                'remove': messages.count() == 0
            }))
        print("Disconnected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        reciever_id = text_data_json['reciever_id']
        sender = User.objects.get(username=self.scope['user'])
        reciever = User.objects.get(id=reciever_id)
        new_message = Message(Sender=sender, message = message, Reciever=reciever)
        new_message.save()
        # Broadcast message to all connected clients
        for client in ChatConsumer.connected_clients:
            if str(client.scope['user']) == reciever.username:
                client.send(text_data=json.dumps({
                    'type': 'message',
                    'id': sender.id,
                    'message': message
                }))
