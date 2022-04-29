from django.urls import path
from user import views

urlpatterns = [
    path('create_user/', views.create_user),
    path('get_user/', views.get_user),
    path("get_patients/", views.get_patients,
         name="get_patients"),
    path("get_doctors/", views.get_doctors,
         name="get_doctors"),
]
