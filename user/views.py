from pydoc import doc
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, Doctor, User
import json


@api_view(['POST'])
def create_user(request):
    """
    Creates user
    """
    data = json.loads(request.body)
    user_name = data['first_name'] + '_' + data['last_name']
    user = User.objects.create(
        firebase_id=data['user_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        username=user_name
    )
    if data['role'] == 1:
        last_patient = Patient.objects.all().last()
        last_doctor = Doctor.objects.all().last()
        Patient.objects.create(
            id=last_patient.id + 1,
            user=user,
            doctor=last_doctor,
            doctor_id=last_doctor.id,

        )
    else:
        last_doctor = Doctor.objects.all().last()
        Doctor.objects.create(
            id=last_doctor.id + 1,
            user=user
        )

    return Response({
        "message": "success",
        "user_id": data['user_id'],
        "pk": user.pk
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_user(request):
    """
    Gets user
    """
    data = json.loads(request.body)
    user = User.objects.get(firebase_id=data['user_id'])
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
            'id': doctor.id,
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
            'id': patient.id,
            'first_name': patient.user.first_name,
            'last_name': patient.user.last_name,
            'phone_number': patient.phone_number,
            'address': patient.address,
            'medical_condition': patient.medical_condition
        })
    return Response(response, status=status.HTTP_200_OK)
