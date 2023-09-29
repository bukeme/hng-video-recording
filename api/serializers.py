from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ['pk', 'video']
		extra_kwargs = {'pk': {'read_only': True}}