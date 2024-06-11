from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','username','email']
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        # Calling the parent class method to get the token
        token = super().get_token(user)
         # Adding username to the token payload
        token['username']= user.username
        # Returning the modified token
        return token
        