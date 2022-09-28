import re
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.utils import timezone

from django.db import models

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('username', max_length=15, unique=True, help_text='Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters',
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid username.', 'invalid')])

    name = models.CharField('name', max_length=255)

    email = models.EmailField('email address', max_length=255, unique=True)

    is_staff = models.BooleanField(
        'staff status', default=False, help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(
        'active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    is_trusty = models.BooleanField(
        'trusty', default=False, help_text='Designates whether this user has confirmed his account.')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'name']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
