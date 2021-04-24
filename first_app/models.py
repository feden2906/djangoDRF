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
    # office = models.OneToOneField(OfficeModel, on_delete=models.CASCADE)                                # One to One    для розширення таблиці
    # offices = models.ForeignKey(OfficeModel, on_delete=models.CASCADE, related_name='employee')         # One to Many   related_name=''  дає можливість з однієї моделі звертатися в іншу (повязану з нею)
    offices = models.ManyToManyField(OfficeModel, related_name="employee", db_column='office_employee')   # Many to Many  db_column=''  створить носу заблицю в якій буде зберігати залежності (id => id)

    class Meta:
        db_table = 'employees'
