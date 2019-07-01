import json

from channels.generic.websocket import JsonWebsocketConsumer

from api.models import Measurement
from receiver.service import create_measurement_from_json


class ReceiverConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        json_message = json.loads(text_data)
        measurement = create_measurement_from_json(json_message)
        Measurement.save(measurement)
