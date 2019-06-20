from rest_framework import serializers

from api import models


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'


class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scanner
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    customer = CustomerSerializer()
    scanner = ScannerSerializer()

    volume_sum = serializers.SerializerMethodField()
    volumes = serializers.SerializerMethodField()

    class Meta:
        model = models.Job
        fields = '__all__'

    def get_volume_sum(self, obj):
        return obj.get_volume_sum()

    def get_volumes(self, obj):
        return obj.get_volumes()


class ConveyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conveyor
        fields = '__all__'
