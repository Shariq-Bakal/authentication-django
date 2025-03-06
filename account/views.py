from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer

class RegisterUserAV(APIView):
    renderer_classes = [UserRenderer] # This way you are going to use renderer class. It should be used inside a class
    def post(self, request):
        #This UserRenderer will help in front end
        serializer = UserRegisterSerializer(data = request.data) # gets data from frontend and serialize it 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        


class UserLoginAV(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password = password) # it will check if there are users in database or not
            if user is not None: 
                return Response({"msg":"Login success"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Fix: Ensure a Response is Always Returned

        

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
