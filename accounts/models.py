from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email,password, dob, **extra_fields):
        """
        create user given email and password
        """
        if not email:
            raise ValueError('Email Must be set')
        
        if not password:
            raise ValueError('Password Must be set')
        
        if not dob:
            raise ValueError('Birthday Must be set')
        
        email = self.normalize_email(email)
        UserModal = get_user_model()
        user = UserModal(email = email,dob=dob, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, dob=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password,dob, **extra_fields)
    

    def create_superuser(self, email=None, password=None, dob=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password,dob, **extra_fields)





class UserType(models.TextChoices):
    ADMIN = 'admin', 'admin'
    MANAGER = 'manager', 'manager'
    SELLER = 'seller', 'seller'

class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), unique=True)
    user_type = models.CharField(_("User Type"), max_length=50,choices=UserType.choices, default=UserType.SELLER)
    image = models.ImageField(_("Image"), upload_to='profile', null=True, blank=True)
    dob = models.DateField(_("Birthday"))
    create = models.DateTimeField(_("Profile Create"), auto_now_add=True)
    update = models.DateTimeField(_("Profile Update"), auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['dob']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'