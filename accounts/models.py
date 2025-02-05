from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=True)


