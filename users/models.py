import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        if password is None:
            raise TypeError('Users must have a password.')
        user = self.model(email=self.normalize_email(email),)
        user.set_first_name(first_name)
        user.set_last_name(last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, password):
    #     user = self.create_user(email, password)
    #     user.is_superuser = True
    #     user.save()
    #     return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = "login"