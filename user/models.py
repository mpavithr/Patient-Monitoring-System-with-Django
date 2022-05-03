from django.contrib.auth.models import AbstractUser
from django.db import models

# from .managers import CustomUserManager


class Doctor(models.Model):
    """
    Model representing a doctor
    """
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    speciality = models.CharField(max_length=100, null=True)


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
    )
    doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    medical_condition = models.CharField(max_length=100, null=True)


class User(AbstractUser):
    """
    Model representing a user
    """

    firebase_id = models.CharField(unique=True, null=True, max_length=100)
    username = models.CharField(max_length=100, null=True, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.username


class PatientDeviceMeasurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE
    )
    machine_id = models.IntegerField(null=False)
    date_assigned = models.DateField(null=False)
    date_returned = models.DateField(null=False)
    measurement = models.FloatField(null=False)

    def __str__(self):
        return str(self.measurement_id, null=False)
