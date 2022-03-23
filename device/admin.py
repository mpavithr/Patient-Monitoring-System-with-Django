from django.contrib import admin

# Register your models here.

from device.models import Device, PatientData

admin.site.register(Device)
admin.site.register(PatientData)
