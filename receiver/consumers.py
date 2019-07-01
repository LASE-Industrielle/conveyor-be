from channels.generic.websocket import JsonWebsocketConsumer
import json


class ReceiverConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        print(json.loads(text_data)['message'])
