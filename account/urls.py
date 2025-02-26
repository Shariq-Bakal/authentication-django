from django.urls import path
from .views import RegisterUserAV

urlpatterns = [
    path("register/", RegisterUserAV.as_view(), name="register"),
]