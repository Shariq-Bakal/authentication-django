from django.urls import path
from .views import RegisterUserAV, UserLoginAV

urlpatterns = [
    path("register/", RegisterUserAV.as_view(), name="register"),
    path("login/",UserLoginAV.as_view(), name="login"),
]