from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from main.models import *
# import sys 

# sys.path.insert(1, '')

# import models.py

@api_view(['GET'])
def getCourse(request):
    
    # sample way to return json object as a get request 
    # response 

    #person = {"name": "hello", "sirNAme":"world"}

    data = request.data

    courseVal = request.query_params.get('courseVal')
    course = Course.objects.get(name=courseVal)
    courseContent = CourseContent.objects.filter(Course=courseVal)

    response = {"course":course, "courseContent":courseContent}


    
    # for i in course:
    #     i['videoURL']

    print(course)

    return Response(response)

@api_view(['POST'])
def addCourse(request):

    # data holds the json sent as part of the post request
    data = request.data

    course = Course(name=data['name'], teacher=data['teacher'])
    course.save()

@api_view(['POST'])
def addCourseContent(request):

    data = request.data

    course = CourseContent.objects.filter(Course=data['course'])
    
    id = course.id

    courseContent = CourseContent(videoURL=data['URL'], textContent = data['textContent'] )
    courseContent.type_id = id

    courseContent.save() 
    print(data)
    return Response()


