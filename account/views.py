from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer

class RegisterUserAV(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data) # gets data from frontend and serialize it 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error':"User wasn't created successfully"})
        

# Create your views here.
# from .serializers import CustomUserSerializer, UserProfileSerializer
# from rest_framework.generics import ListCreateAPIView
# from .models import User, UserProfile

# class ListUsers(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = CustomUserSerializer

# class ListProfiles(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
