from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Username',
        null=True,
        db_index=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
        db_index=True
    )
    role = models.CharField(
        max_length=30,
        verbose_name='Роль пользователя',
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя',
        null=True
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        null=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_admin_or_moderator(self):
        return self.role in [self.Role.ADMIN, self.Role.MODERATOR]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        ordering = ['username']
        verbose_name = 'user'
        verbose_name_plural = 'users'
