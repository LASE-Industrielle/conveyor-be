from rest_framework import viewsets

from api import models, serializers


class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer


class ConveyorViewSet(viewsets.ModelViewSet):
    queryset = models.Conveyor.objects.all()
    serializer_class = serializers.ConveyorSerializer
