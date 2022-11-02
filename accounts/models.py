from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from kanji.models import *

from .managers import CustomUserManager

# Create your models here.

choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    grade = models.IntegerField(choices=choices, default=1)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def next_grade(self):
        n_grade = self.grade + 1
        if n_grade in range(1, 8):
            self.grade = n_grade
            self.save()
