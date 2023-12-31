from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import CustomUser
from home.serializers import *

from rest_framework.views import APIView

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['flask', 'Django', 'Tornado', 'FastApi'],
        'course_provider' : 'Scaler'
    }

    if request.method == 'GET':
        print(request.GET.get('search'))
        print('겟메서드로 접근 중')
        
    elif request.method == 'POST':
        print('포스트 메서드로 접근중')
        data = request.data
        print(data)
        print(data['name'])


    elif request.method == 'PUT':
        print('풋 메서드로 접근중')

    return Response(courses)


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message':f'success'})

    return Response(serializer.errors)


class UserAPI(APIView):
    def get(self, request):
        return Response({"message": "겟 방식 요청 확인"})

    def post(self, request):
        return Response({"message": "post 방식 요청 확인"})
    
    def put(self, request):
        return Response({"message": "put 방식 요청 확인"})
    
    def patch(self, request):
        return Response({"message": "patch 방식 요청 확인"})
    
    def delete(self, request):
        return Response({"message": "delete 방식 요청 확인"})
    


@api_view(["GET","POST", 'PUT', 'PATCH', "DELETE"])
def Person(request):
    if request.method == 'GET':
        objs = CustomUser.objects.all()
        serializer = UserSerializer(objs, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = CustomUser.objects.get(id = data['id'])
        serializer = UserSerializer(obj, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        data = request.data
        obj = CustomUser.objects.get(id = data["id"])
        obj.delete()
        return Response({'message':f'user {obj.name} deleted'})