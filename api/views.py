from rest_framework import generics, mixins
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import VideoSerializer
from .models import Video
from .utils import video_transcription


class VideoAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
	parser_classes = [FormParser, MultiPartParser]

	def get(self, request, *args, **kwargs):
		if kwargs.get('pk'):
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		obj = serializer.save()
		obj.transcription = video_transcription(obj.video.url)
		obj.save()