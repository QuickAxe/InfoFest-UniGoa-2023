from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from main.models import *
from api.serializer import *



@api_view(['GET'])
def getCourse(request):
   
    data = request.data
    courseVal = request.query_params.get('courseVal')

    print(courseVal)
    
    course = Course.objects.get(pk=courseVal)
    courseContent = CourseContent.objects.filter(Course=courseVal)

    response = []
    
    # response.append({"TeacherName":course.Teacher.name})
    course = CourseSerializer(course)

    response.append(course.data)

    for s in courseContent:
        s = CourseContentSerializer(s)
        response.append(s.data)

    return Response(response)

@api_view(['POST'])
def addCourse(request):

    # data holds the json sent as part of the post request
    data = request.data

    teacher = Teacher.objects.get(name=data['teacher'])
    course = Course(name=data['name'], Teacher=teacher)
    course.save()

    return Response()

@api_view(['POST'])
def addCourseContent(request):

    data = request.data
    course = Course.objects.get(name=data['course'])
    
    id = course.id

    courseContent = CourseContent(Course = course, videoURL=data['URL'], textContent = data['textContent'] )
    courseContent.pk = id

    courseContent.save()
    return Response()

# @api_view(['GET'])
# def get(request):
#     course = Course.objects.filter()
#     print(course[0].pk)
#     return Response()
