from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Patient, Doctor
import json


@api_view(['GET'])
def get_list_of_patients(request):
    """
    List list of all patients
    """
    print(request)
    doctor_id = request.GET.get('doctor_id')
    patients = Patient.objects.filter(doctor_id=doctor_id)
    response = []
    print(patients)
    for patient in patients:
        response.append({
            'id': patient.id,
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'phone_number': patient.phone_number,
            'address': patient.address,
            'medical_condition': patient.medical_condition
        })
    return json.dumps(response)


@api_view(['GET'])
def get_doctor_by_patient_id(request):
    """
    List list of all patients
    """
    patient_id = request.GET.get('patient_id')
    doctor = Doctor.objects.get(patient_id=patient_id)
    return json.dumps({
        'id': doctor.id,
        'first_name': doctor.first_name,
        'last_name': doctor.last_name,
        'phone_number': doctor.phone_number,
        'address': doctor.address,
        'speciality': doctor.speciality
    })
