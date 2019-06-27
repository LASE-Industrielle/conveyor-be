from rest_framework import serializers

from api import models


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = models.Job
        fields = '__all__'



class ConveyorSerializer(serializers.ModelSerializer):
    job_set = JobSerializer(many=True)

    class Meta:
        model = models.Conveyor
        fields = '__all__'
