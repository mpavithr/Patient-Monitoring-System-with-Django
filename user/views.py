from pydoc import doc
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, Doctor, User, PatientDeviceMeasurement
import json
import datetime


@api_view(['POST'])
def create_user(request):
    """
    Creates user
    """
    data = json.loads(request.body)
    user_name = data['userId']
    user = User.objects.create(
        firebase_id=data['userId'],
        first_name=data['firstname'],
        last_name=data['lastname'],
        email=data['email'],
        username=user_name
    )
    if data['role'] == "1":
        last_patient = Patient.objects.all().last()
        last_doctor = Doctor.objects.all().last()
        try:
            last_id = last_patient.id + 1
        except:
            last_id = 0
        Patient.objects.create(
            id=last_id,
            user=user,
            doctor=last_doctor,
            doctor_id=last_doctor.id,

        )
    else:
        last_doctor = Doctor.objects.all().last()
        try:
            last_id = last_doctor.id + 1
        except:
            last_id = 0
        Doctor.objects.create(
            id=last_id,
            user=user
        )

    return Response({
        "message": "success",
        "user_id": data['userId'],
        "pk": user.pk
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_user(request):
    """
    Gets user
    """
    data = json.loads(request.body)
    user = User.objects.get(firebase_id=data['userId'])
    try:
        Patient.objects.get(user=user)
        role = 1
    except Patient.DoesNotExist:
        role = 2

    return Response({
        "message": "success",
        "user_id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": role
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_doctors(request):
    """
    List list of all patients
    """
    doctors = Doctor.objects.all()
    response = []
    for doctor in doctors:
        response.append({
            'id': doctor.user.firebase_id,
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name,
            'phone_number': doctor.phone_number,
            'address': doctor.address,
            'speciality': doctor.speciality
        })
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_patients(request):
    """
    List list of all patients
    """
    patients = Patient.objects.all()
    response = []
    for patient in patients:
        response.append({
            'id': patient.user.firebase_id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name,
            'phone_number': patient.phone_number,
            'address': patient.address,
            'medical_condition': patient.medical_condition,
            'measurements': []
        })
        measurements = PatientDeviceMeasurement.objects.filter(patient=patient)
        for measurement in measurements:
            response[-1]['measurements'].append({
                'measurement_id': measurement.measurement_id,
                'machine_id': measurement.machine_id,
                'date_assigned': str(measurement.date_assigned),
                'date_returned': str(measurement.date_returned),
                'measurement': measurement.measurement
            })
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_patient_device_measurement(request):
    """
    Creates patient device measurement
    """
    data = json.loads(request.body)
    user = User.objects.get(firebase_id=data['patient_id'])
    patient = Patient.objects.get(user=user)
    PatientDeviceMeasurement.objects.create(
        patient=patient,
        machine_id=data['machineid'],
        date_assigned=data['dateAssigned'],
        date_returned=data['dateReturned'],
        measurement=data['measurement']
    )
    return Response({
        "message": "success"
    }, status=status.HTTP_200_OK)
