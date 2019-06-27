from django.contrib import admin

from api.models import Conveyor, Job, Measurement, Material, Customer

admin.site.register(Conveyor)
admin.site.register(Job)
admin.site.register(Measurement)
admin.site.register(Material)
admin.site.register(Customer)
