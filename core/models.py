from django.db import models





# Расходы дома
class Expenses(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)
    money = models.BigIntegerField('Сумма')