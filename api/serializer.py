from rest_framework import serializers
from main.models import *

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    Teacher = serializers.CharField(max_length=50)

    # class Meta:
    #     model = Course
    #     fields = "__all__"


class CourseContentSerializer(serializers.Serializer):
    videoURL = serializers.URLField()
    textContent = serializers.CharField(max_length = 500)

    # class Meta:
    #     model = CourseContent
    #     fields = "__all__"

class QuizContentSerializer(serializers.Serializer):
    
    q1 = serializers.CharField(max_length=100)

#-----------------------------------------------------
    q1A = serializers.CharField(max_length=100)
    q1B = serializers.CharField(max_length=100)
    q1C = serializers.CharField(max_length=100)
    q1D = serializers.CharField(max_length=100)
#-----------------------------------------------------
    correctAns = serializers.IntegerField(default=3)
