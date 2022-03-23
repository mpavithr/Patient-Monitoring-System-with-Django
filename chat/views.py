from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from chat.serializers import ChatSerializer
from chat.models import Chat
from django_q.tasks import async_task

# Create your views here.


class ListChatAPIView(ListAPIView):
    """This endpoint list all of the available chats from the database"""
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class CreateChatAPIView(CreateAPIView):
    """This endpoint allows for creation of a chat"""
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class UpdateChatAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific chat by passing in the id of the chat to update"""
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class DeleteChatAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Chat from the database"""
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


@api_view(['POST'])
def convert_speech_to_text(request):
    """
    List all chats, or create a new chat.
    """
    async_task('chat.tasks.speech_to_text', request.data['speech_file'])
