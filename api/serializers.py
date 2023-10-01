from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ['pk', 'video', 'transcription']
		extra_kwargs = {'pk': {'read_only': True}, 'transcription': {'required': False, 'read_only': True}}