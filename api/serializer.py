from rest_framework import serializers
from main.models import *

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    # class Meta:
    #     model = Course
    #     fields = "__all__"


class CourseContentSerializer(serializers.Serializer):
    videoURL = serializers.URLField()
    textContent = serializers.CharField(max_length = 500)

    # class Meta:
    #     model = CourseContent
    #     fields = "__all__"
