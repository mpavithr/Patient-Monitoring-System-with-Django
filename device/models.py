from django.db import models

# Create your models here.


class Device(models.Model):
    device_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    firmware_version = models.FloatField(null=False)
    date_of_purcahse = models.DateField(null=False)
    serial_number = models.CharField(max_length=100, null=False)
    mac_address = models.CharField(max_length=100, null=True)
    machine_id = models.IntegerField(null=False)

    def __str__(self):
        return str(self.device_id, null=False)


class PatientData(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    device_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    assigner_id = models.IntegerField(null=False)
    machine_id = models.IntegerField(null=False)
    date_assigned = models.DateField(null=False)
    date_returned = models.DateField(null=False)
    measurement = models.FloatField(null=False)

    def __str__(self):
        return str(self.measurement_id, null=False)
