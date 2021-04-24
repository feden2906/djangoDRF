from django.db import models


# Create your models here.

class OfficeModel(models.Model):
    name = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = 'offices'


class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField
    city = models.CharField(max_length=30)
    office = models.OneToOneField(OfficeModel, on_delete=models.CASCADE)          # One to One    для розширення таблиці

    class Meta:
        db_table = 'employees'
