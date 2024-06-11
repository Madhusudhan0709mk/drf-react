from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer,UserSerializer

# from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    querset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class RoutesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        routes = [
            '/api/login/',
            '/api/register/',
            '/api/token/refresh/'
        ]
        return Response(routes)
     
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token/',
#         '/api/register/',
#         '/api/token/refresh/'
#     ]
   
#     return Response(routes)
