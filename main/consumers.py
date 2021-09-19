import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime
from .models import Message
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name = 'chat_%s' % self.room_name
        self.room_group_name = 'chat_public'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['name']
        timedate = str(datetime.datetime.now())[:-10]

        # Send message to room group
        message_obj = Message.objects.create(name=username, content=message)
        message_obj.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'name': username,
                'message': message,
                'time': timedate
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['name']
        timedate = event['time']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'name': username,
            'time': timedate,
        }))
