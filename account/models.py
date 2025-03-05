from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
#This class is responsible for managing user creation (both normal users and superusers).
class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,role, name, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), #It converts the email to lowercase 
            date_of_birth=date_of_birth,
            name = name,
            role = role
        )

        user.set_password(password) # This is going to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, date_of_birth, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            name = name,
            role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin','Admin'),
    )
    #The first value in each pair (like 'buyer', 'seller', 'admin') is the value that gets stored in the database.
    #The second value (like 'Buyer', 'Seller', 'Admin') is just a human-readable label that is displayed in the admin panel or elsewhere.

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager() # this creates users and saves data to database

    USERNAME_FIELD = "email" # This treat email as username
    REQUIRED_FIELDS = ["date_of_birth","name", "role"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin # This gives permission to admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserProfile(models.Model):
    user_info = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    username = models.CharField(max_length=22)
    #image
    #location