from django.db import models
from users.models import CustomUser, HouseUser


# Расходы дома
class Expenses(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)
    category = models.ForeignKey('CatExpenses', on_delete=models.PROTECT, verbose_name="Категория расходов", default=1)
    name = models.ForeignKey('ProductName', on_delete=models.PROTECT, verbose_name="Наименование продукта", default=1)
    volume = models.IntegerField('Кличество, объем')
    money = models.BigIntegerField('Сумма')
    status = models.BooleanField('Статус покупки, исполнена или нет')
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, verbose_name="Пользователь", default=1)
    home = models.ForeignKey('HouseUser', on_delete=models.PROTECT, verbose_name="Дом", default=1)



#Категории расходов
class CatExpenses(models.Model):
    category = models.CharField('Название категории', max_length=50)

class ProductName(models.Model):
    name = models.CharField('Наименование продукта', max_length=100)
