

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import Registration


class RegistrationListAPIView(APIView):
    """Handle registration API - List all or Create new"""
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Registration successful!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationDetailAPIView(APIView):
    """Handle single registration - Get, Update or Delete"""
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return None

    def get(self, request, pk):
        registration = self.get_object(pk)
        if not registration:
            return Response(
                {'error': 'Registration not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)

    def put(self, request, pk):
        registration = self.get_object(pk)
        if not registration:
            return Response(
                {'error': 'Registration not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Registration updated successfully!',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        registration = self.get_object(pk)
        if not registration:
            return Response(
                {'error': 'Registration not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        registration.delete()
        return Response(
            {'message': 'Registration deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT
        )