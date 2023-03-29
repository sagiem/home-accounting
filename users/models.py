from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    roles = models.ForeignKey('RoleUsers', on_delete=models.PROTECT, verbose_name="Роль", default=1)
    home = models.ForeignKey('HouseUser', on_delete=models.PROTECT, verbose_name="Дом", default=1)

    def __str__(self):
        return self.username


class RoleUsers(models.Model):
    role = models.CharField('Название роли', max_length=50)

class HouseUser(models.Model):
    name = models.CharField('Название дома', max_length=50)


