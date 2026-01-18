from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):        # custom user manager to handle email-based user creation
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            return ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)     # hash the password
        user.save(using=self._db)       # save the user to the database
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    


class CustomUser(AbstractUser):
    username = None  #  email as the unique identifier
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_authorized = models.BooleanField(default=False)

    # user roles
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'        # forces email as login identifier
    REQUIRED_FIELDS = []  # email & password are required by default

    objects = CustomUserManager()   # use the custom user manager (for email-based creation)

    # Set related_name to None to prevent reverse relationship creation
    groups = models.ManyToManyField(
        'auth.Group',               # Django's built-in Group model
        related_name='+',          # Prevent reverse relationship by using '+' it 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',          # Django's built-in Permission model
        related_name='+',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )