from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    fullname = models.CharField(max_length=100, null=True, blank=True, verbose_name='fullname')
    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    email = models.EmailField(max_length=155, unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False, verbose_name='Joining Date')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin