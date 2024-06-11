from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from .views import UserCreateView,MyTokenObtainPairView,RoutesAPIView
# from rest_framework.decorators import api_view
from . import views
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
    path('register/',UserCreateView.as_view(),name='register'),
    path('login/',MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]
