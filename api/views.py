from rest_framework.response import Response 
from rest_framework.decorators import api_view 


@api_view(['GET'])
def getData(request):
    
    # sample way to return json object as a get request 
    # response 

    person = {'name': 'hello', 'sirNAme':'world'}
    
    return Response(person)


