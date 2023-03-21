from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    phone = models.CharField(max_length=255, verbose_name="Телефон")

    def __str__(self):
        return self.username
