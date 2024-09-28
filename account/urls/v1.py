from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser, TimeStampedModel):
    phone = models.CharField(unique=True)
    is_visible = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    email = None