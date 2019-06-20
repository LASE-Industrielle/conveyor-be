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


class Scanner(models.Model):
    name = models.CharField(max_length=200, default="")
    conveyor = models.ForeignKey(Conveyor, on_delete=models.CASCADE)

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
    belt_speed = models.FloatField(default=0)

    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.external_id} ({self.get_volume_sum()} / {self.target} @ {self.belt_speed} m3/s)'

    def get_volume_sum(self):
        return sum(volume.value for volume in self.volume_set.all())


class Volume(models.Model):
    value = models.FloatField(default=0)
    timestamp = models.DateTimeField(null=True)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}; Recorded: {self.timestamp}; Job ID: {self.job.id}'
