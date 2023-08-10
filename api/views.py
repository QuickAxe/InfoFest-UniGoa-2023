from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from main.models import *
from api.serializer import *
from rest_framework.renderers import JSONRenderer
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

    print(courseVal)
    
    course = Course.objects.get(pk=courseVal)
    courseContent = CourseContent.objects.filter(Course=courseVal)

    course = CourseSerializer(course)
    courseContent = CourseContentSerializer(courseContent)


    course.update(courseContent)
    # for i in course:
    #     i['videoURL']
    response = JSONRenderer().render(course)

    



    # response = json.dumps(response)
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

@api_view(['GET'])
def get(request):
    course = Course.objects.filter()
    print(course[0].pk)
    return Response()
