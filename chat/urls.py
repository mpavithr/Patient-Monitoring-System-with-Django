from django.urls import path
from chat import views

urlpatterns = [
    path("<int:pk>/", views.ListChatAPIView.as_view(), name="chat_list"),
    path("", views.CreateChatAPIView.as_view(), name="chat_create"),
    path("update/<int:pk>/", views.UpdateChatAPIView.as_view(), name="update_chat"),
    path("delete/<int:pk>/", views.DeleteChatAPIView.as_view(), name="delete_chat"),
    # path("speech_to_text/", views.convert_speech_to_text, name="speech_to_text"),
]
