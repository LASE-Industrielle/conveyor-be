from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
# Automatically creates and saves the token for every newly registered user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Conveyor(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Job(models.Model):
    external_id = models.CharField(max_length=200, default="")
    target = models.FloatField(default=0)

    conveyor = models.ForeignKey(Conveyor, on_delete=models.CASCADE, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Measurement(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    conveyor_speed = models.FloatField(default=0)
    material_density = models.FloatField(default=0)
    area = models.FloatField(default=0)
    volume_sum = models.FloatField(default=0)
    volume_stream = models.FloatField(default=0)
    mass_sum = models.FloatField(default=0)
    mass_stream = models.FloatField(default=0)
    conveyor_deviation = models.FloatField(default=0)
    count_valid_pts = models.FloatField(default=0)
    total_area = models.FloatField(default=0)
    volume_stream_upper_limit = models.FloatField(default=0)
    volume_stream_lower_limit = models.FloatField(default=0)
