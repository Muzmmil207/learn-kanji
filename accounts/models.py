from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from kanji.models import *
from .managers import CustomUserManager
# Create your models here.

choices = (
    ('first', 'first'),
    ('second', 'second'),
    ('third', 'third'),
    ('fourth', 'fourth'),
    ('fifth', 'fifth'),
    ('sixth', 'sixth'),
    ('seventh', 'seventh'),
)

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    grade = models.CharField(max_length=7, choices=choices, default=choices[0])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def next_grade(self):
        
        self.grade=choices[1]
        self.save()

