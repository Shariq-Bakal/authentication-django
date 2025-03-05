from .models import UserProfile, User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True) # this will serializer password and show password in dotted format
    pass
    class Meta:
        model = User
        fields = ['name','date_of_birth','email','role','password','password2']
        extra_kwargs = {
            'password':{'write_only':True} # this will not let password update
        }
    def validate(self, attrs):
        # first we validate password
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        print(attrs)
        print(password2)
        if password != password2:
            raise serializers.ValidationError("Both password and confirm password must be same")
        return attrs
    def create(self, validated_data):
        return User.objects.create(**validated_data) # this will create our user
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ["bio"]
    
# class CustomUserSerializer(serializers.ModelSerializer):
#     profile = UserProfileSerializer()  # Nest UserProfileSerializer here
#     class Meta:
#         model = User
#         fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255) # first serialize it If you remove this line, the serializer will no longer know how to handle the email field in terms of validation and formatting. In that case, you could:
    class Meta:
        model = User
        fields = ['email','password'] #This line tells the serializer which fields from the User model you want to include for serialization or validation.
    