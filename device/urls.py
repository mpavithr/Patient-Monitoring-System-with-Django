from django.urls import path
from device import views

urlpatterns = [
    path("<int:pk>/", views.ListDeviceAPIView.as_view(), name="device_list"),
    path("", views.CreateDeviceAPIView.as_view(), name="device_create"),
    path("update/<int:pk>/", views.UpdateDeviceAPIView.as_view(),
         name="update_device"),
    path("delete/<int:pk>/", views.DeleteDeviceAPIView.as_view(),
         name="delete_device"),
    path("patient_data/<int:pk>/", views.ListPatientDataAPIView.as_view(),
         name="patient_data_list"),
    path("patient_data/", views.CreatePatientDataAPIView.as_view(),
         name="patient_data_create"),
    path("patient_data/update/<int:pk>/",
         views.UpdatePatientDataAPIView.as_view(), name="patient_data_update"),
    path("patient_data/delete/<int:pk>/",
         views.DeletePatientDataAPIView.as_view(), name="patient_data_delete"),
]
