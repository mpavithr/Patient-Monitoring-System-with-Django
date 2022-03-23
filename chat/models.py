from django.db import models

# Create your models here.


class Chat(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender_id = models.IntegerField(null=False)
    receiver_id = models.IntegerField(null=False)
    text = models.TextField(null=False)
    attachment_audio_url = models.TextField(null=True)
    attachment_image_url = models.TextField(null=True)
    attachment_video_url = models.TextField(null=True)
    attachment_document_url = models.TextField(null=True)

    def __str__(self):
        return str(self.chat_id)
