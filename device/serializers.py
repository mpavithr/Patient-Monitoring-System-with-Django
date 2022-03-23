from rest_framework import serializers
from device.models import Device, PatientData


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = "__all__"
