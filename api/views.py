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

    crsVal = request.query_params.get('crsVal')

    crs = CourseContent.objects.filter(Course=crsVal)

    print(crs)









    return Response()

@api_view(['POST'])
def addCourse(request):

    # data holds the json sent as part of the post request
    data = request.data

    

    print(data)

    return Response()


