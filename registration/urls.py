from django.urls import path
from .views import RegistrationListAPIView, RegistrationDetailAPIView

urlpatterns = [
    path('', RegistrationListAPIView.as_view(), name='registration-list'),
    path('<int:pk>/', RegistrationDetailAPIView.as_view(), name='registration-detail'),
]
