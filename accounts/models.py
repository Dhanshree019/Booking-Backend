from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy

# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, phone_number=None, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(phone_number, password, **other_fields)

    def create_user(self, phone_number=None, password=None, **other_fields):

        if phone_number == None:
            raise ValueError(gettext_lazy('You must provide an phone_number'))

        user = self.model(phone_number=phone_number, **other_fields)

        if password is not None:
            user.set_password(password)

        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    phone_number = models.CharField(max_length=16, unique=True)
    full_name = models.CharField(max_length=64, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return self.phone_number
