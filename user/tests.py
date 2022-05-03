from django.test import TestCase
from .models import Doctor, Patient, User, PatientDeviceMeasurement

# Create your tests here.


class CreateUserTestCase(TestCase):
    def setUp(self):
        user1 = User(
            firebase_id="123",
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            username="123"
        )
        user1.save()
        user1 = User.objects.get(firebase_id="123")
        user2 = User(
            firebase_id="456",
            first_name="Jane",
            last_name="Doe",
            email="janedoe@gmail.com",
            username="456"
        )
        user2.save()
        user2 = User.objects.get(firebase_id="456")
        doctor = Doctor(
            user=user1,
            phone_number="1234567890",
            address="123 Main St",
            speciality="Cardiology"
        )
        doctor.save()
        doctor = Doctor.objects.get(user__firebase_id="123")
        patient = Patient(
            user=user2,
            doctor=doctor,
            doctor_id=doctor.id,
            phone_number="1234567890",
            address="123 Main St",
            medical_condition="Heart Disease"
        )
        patient.save()
        patient = Patient.objects.get(user__firebase_id="456")
        patient_device_measurement = PatientDeviceMeasurement(
            measurement_id=1,
            patient=patient,
            patient_id=patient.id,
            machine_id=1,
            date_assigned="2020-01-01",
            date_returned="2020-01-01",
            measurement=1.0
        )
        patient_device_measurement.save()

    def test_user_creation(self):
        user1 = User.objects.get(firebase_id="123")
        self.assertEqual(user1.first_name, "John")
        self.assertEqual(user1.last_name, "Doe")
        self.assertEqual(user1.email, "johndoe@gmail.com")
        self.assertEqual(user1.username, "123")

    def test_doctor_creation(self):
        doctor = Doctor.objects.get(user__firebase_id="123")
        self.assertEqual(doctor.phone_number, "1234567890")
        self.assertEqual(doctor.address, "123 Main St")
        self.assertEqual(doctor.speciality, "Cardiology")

    def test_patient_creation(self):
        patient = Patient.objects.get(user__firebase_id="456")
        self.assertEqual(patient.phone_number, "1234567890")
        self.assertEqual(patient.address, "123 Main St")
        self.assertEqual(patient.medical_condition, "Heart Disease")

    def test_patient_device_measurement_creation(self):
        patient_device_measurement = PatientDeviceMeasurement.objects.get(
            measurement_id=1)
        self.assertEqual(patient_device_measurement.measurement, 1.0)
        self.assertEqual(
            patient_device_measurement.patient.user.firebase_id, "456")
        self.assertEqual(
            patient_device_measurement.patient.doctor.user.firebase_id, "123")
