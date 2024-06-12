from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import *
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','username','email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        # Calling the parent class method to get the token
        token = super().get_token(user)
         # Adding username to the token payload
        token['username']= user.username
        # Returning the modified token
        return token

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super(CategorySerializer,self).__init__(*args, **kwargs)
    #     request = self.context.get(request)
    #     if request and request.method == 'POST':
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 3
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'
        

            
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields='__all__'

        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields='__all__'
        

            
class AuthorSerializer(serializers.Serializer):
    views = serializers.IntegerField(default=0)
    posts = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    bookmarks = serializers.IntegerField(default=0)