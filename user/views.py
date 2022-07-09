from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from certification.models import Certification
from argon2 import PasswordHasher
from user_service.validators import validate_password

@api_view(['POST'])
def insert_users(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid() and request.data['cert_id'] and request.data['plain_password']:
            certification = Certification.objects.filter(id=request.data['cert_id'], phone_number=request.data['phone_number'], certified=1)
            validate_password(request.data['plain_password'])

            if certification.count():
                password = PasswordHasher().hash(request.data['plain_password'])
                serializer.save()
                User.objects.filter(id=serializer.data["id"]).update(password=password)
                
                return Response(serializer.data)    
    

@api_view(['GET'])
def count_users(request, value):
    data = {'message': ""}

    if request.method == 'GET':
        count = User.objects.filter(email=value).count()
        data['email'] = count
            
        count = User.objects.filter(phone_number=value).count()
        data['phone_number'] = count

        return Response(data, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, id):
    data = {'message': ""}

    if request.method == 'GET':
        serializer = UserSerializer(User.objects.filter(id=id).get())

        data['data'] = {
            'user': serializer.data
        }

        return Response(data, status.HTTP_200_OK)
    

