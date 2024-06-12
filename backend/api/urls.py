from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from .views import *
# from rest_framework.decorators import api_view
from . import *
from rest_framework.permissions import AllowAny
# from rest_framework.reverse import reverse
# @api_view(['GET'])
# def api_root(request):
#     """
#     API Root
    
#     Welcome to the API root for the LMS project.
#     """
#     return Response({'register':reverse('register',request=request),
#                      'Login':reverse('token_obtain_pair',request=request),
#                      'Token refresh':reverse('token_refresh',request=request),
#                      })
# api_root.permission_classes = [AllowAny]
urlpatterns = [
    # path('',views.getRoutes),
    path('', RoutesAPIView.as_view(),name='routes'),
    path('user/register/',UserCreateView.as_view(),name='register'),
    path('user/login/',MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('user/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('user/profile/<user_id>/',ProfileRetriveUpdateAPIView.as_view(),name='user_profile'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    
    path('post/category/list/',CategoryListAPIView.as_view(),name='list_category'),
    path('post/category/posts/<slug>/', PostCategoryListAPIView.as_view()),
    path('post/lists/',PostAPIView.as_view(),name='posts_list'),
    path('post/detail/<slug>/',PostDetailAPIView.as_view(),name='post-detail'),
]
