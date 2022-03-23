from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from device.serializers import DeviceSerializer, PatientDataSerializer
from device.models import Device, PatientData

# Create your views here.


class ListDeviceAPIView(ListAPIView):
    """This endpoint list all of the available devices from the database"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CreateDeviceAPIView(CreateAPIView):
    """This endpoint allows for creation of a device"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class UpdateDeviceAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific device by passing in the id of the device to update"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeleteDeviceAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Device from the database"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class ListPatientDataAPIView(ListAPIView):
    """This endpoint list all of the available patient data from the database"""
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer


class CreatePatientDataAPIView(CreateAPIView):
    """This endpoint allows for creation of a patient data"""
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer


class UpdatePatientDataAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific patient data by passing in the id of the patient data to update"""
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer


class DeletePatientDataAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Patient data from the database"""
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
