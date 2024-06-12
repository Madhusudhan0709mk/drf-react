from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import request
from .serializers import *


from rest_framework import status
# from django.conf import settings
from django.contrib.auth import get_user_model

import json
import random
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
            '/api/user/login/',
            '/api/user/register/',
            '/api/user/token/refresh/',
            '/api/user/profile/<user_id>/',
            'post/category/list/',
            'post/category/posts/<slug>/',
            'post/lists/'
        ]
        return Response(routes)


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=205)
        except Exception as e:
            return Response(status=400)     
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token/',
#         '/api/register/',
#         '/api/token/refresh/'
#     ]
   
#     return Response(routes)

# profile view
class ProfileRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class= ProfileSerializer
  
    permission_classes = [IsAuthenticated]
    
    def get_query(self):
        user_id = self.kwargs['user_id']
        
        user = User.objects.get(id=user_id)
        # profile = Profile.objects.get(user=user)
        return Profile.objects.get(user=user)


# list all categories
class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all()

# detail post view of particular category  
class PostCategoryListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug_catgory = self.kwargs['slug']
        category=Category.objects.get(slug=slug_catgory)
        return Post.objects.filter(category=category)
    
# list all post view 
class PostAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny,]
    
    def get_queryset(self):
        return Post.objects.all()

# detail post view
class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny,]
    
    def get_object(self):
        slug = self.kwargs['slug']
        post = Post.objects.get(slug=slug)
        post.view += 1
        post.save() 
        return post
    
# list like count for post view

class LikePostAPIView(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        post_id = request.data['post_id']

        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)

        # Check if post has already been liked by this user
        if user in post.likes.all():
            # If liked, unlike post
            post.likes.remove(user)
            return Response({"message":"post diliked"},status = status.HTTP_200_OK)
        else:
            post.likes.add(user)
            Notification.objects.create(
                user=post.user,
                post=post,
                type="Like",
            )
            return Response({"message": "Post Liked"}, status=status.HTTP_201_CREATED)
 
# comment create view   
class PostCommentAPIView(APIView):
    def post(self, request):
        # Get data from request.data (frontend)
        post_id = request.data['post_id']
        name = request.data['name']
        email = request.data['email']
        comment = request.data['comment']

        post = Post.objects.get(id=post_id)

        # Create Comment
        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            comment=comment,
        )

        # Notification
        Notification.objects.create(
            user=post.user,
            post=post,
            type="Comment",
        )

        # Return response back to the frontend
        return Response({"message": "Commented Sent"}, status=status.HTTP_201_CREATED)
 
class BookmarkPostAPIView(APIView):
    
    def post(self, request):
        user_id = request.data['user_id']
        post_id = request.data['post_id']

        user = User.objects.get(id=user_id)
        post =Post.objects.get(id=post_id)

        bookmark =Bookmark.objects.filter(post=post, user=user).first()
        if bookmark:
            # Remove post from bookmark
            bookmark.delete()
            return Response({"message": "Post Un-Bookmarked"}, status=status.HTTP_200_OK)
        else:
            Bookmark.objects.create(
                user=user,
                post=post
            )

            # Notification
            Notification.objects.create(
                user=post.user,
                post=post,
                type="Bookmark",
            )
            return Response({"message": "Post Bookmarked"}, status=status.HTTP_201_CREATED)

