from rest_framework.response import Response 
from rest_framework.decorators import api_view 


@api_view(['GET'])
def getData(request):
    
    # sample way to return json object as a get request 
    # response 

    #person = {"name": "hello", "sirNAme":"world"}

    data = request.data
    
    return Response(person)

@api_view(['POST'])
def addItem(request):

    # data holds the json sent as part of the post request
    data = request.data
    print(data)

    return Response()


