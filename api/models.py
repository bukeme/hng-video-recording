from django.db import models
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

# Create your models here.

class Video(models.Model):
	video = models.FileField(upload_to='video/%Y-%m-%d', storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
	transcription = models.TextField(null=True, blank=True)
