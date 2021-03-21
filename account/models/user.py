from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from ContactInformation.models import BaseModel

__all__ = ['User']


class UserManager(BaseUserManager):
    """
    Override base user manger to add create user functionality.
    """

    def create_user(self, phone_number: int, user_name: str, password: str,
                    email: str = None) -> object:
        """
        A method which functionality to create user.

        :param phone_number: User phone number required for login
        :param user_name: User display name
        :param password: USer authentication password
        :param email: User email address
        :return: User object
        """
        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            user_name=user_name
        )

        # Store user password in hash
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, *args: list, **kwargs: dict) -> object:
        """
        A method which functionality to create django super admin user.

        :param args: List of position argument.
        :param kwargs: Dictionary contain method keyword argument.
        :return: User object
        """
        # Create user
        user = self.create_user(*args, **kwargs)

        # Set super django admin flag
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    user_name = models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(unique=True)
    email = models.EmailField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.user_name
