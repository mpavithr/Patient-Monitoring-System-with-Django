from django.urls import path
from user import views

urlpatterns = [
    path("get_list_of_patients/", views.get_list_of_patients,
         name="get_list_of_patients"),
    path("get_doctor_by_patient_id/", views.get_doctor_by_patient_id,
         name="get_doctor_by_patient_id"),
]
