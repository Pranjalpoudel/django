from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from .views import DashboardAPIView

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/dashboard/', DashboardAPIView.as_view()),
]
