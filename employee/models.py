from django.db import models

from office.models import OfficeModel


class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField
    city = models.CharField(max_length=30)
    offices = models.ForeignKey(OfficeModel, on_delete=models.CASCADE, related_name='employee')            # One to Many   related_name=''  дає можливість з однієї моделі звертатися в іншу (повязану з нею)

    class Meta:
        db_table = 'employees'
