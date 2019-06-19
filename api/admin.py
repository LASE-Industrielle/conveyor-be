from django.contrib import admin

from api.models import Conveyor, Scanner, Job, Volume, Material, Customer

admin.site.register(Conveyor)
admin.site.register(Scanner)
admin.site.register(Job)
admin.site.register(Volume)
admin.site.register(Material)
admin.site.register(Customer)
