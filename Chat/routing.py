from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from ChatApp.Chat import ChatConsumer
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', ChatConsumer.as_asgi()),
    ])
})