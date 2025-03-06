from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user) #RefreshToken.for_user(user) creates a refresh token for the given user.
    print(refresh)
    print(user)
    #This function generates authentication tokens (refresh & access tokens) for a user in a Django application using JWT (JSON Web Tokens).

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterUserAV(APIView):
    renderer_classes = [UserRenderer] # This way you are going to use renderer class. It should be used inside a class
    def post(self, request):
        #This UserRenderer will help in front end
        serializer = UserRegisterSerializer(data = request.data) # gets data from frontend and serialize it 
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            #we need to call token generation code here
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'user created successfully'}, status=status.HTTP_201_CREATED)
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
                #generate token when user is valid 
                token = get_tokens_for_user(user)
                return Response({"token": token,"msg":"Login success"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        
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
