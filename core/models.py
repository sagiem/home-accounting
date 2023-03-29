from django.db import models


# Доходы дома
class Income(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)



# Расходы дома
class Expenses(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)