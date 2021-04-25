from rest_framework.serializers import ModelSerializer

from employee.models import EmployeeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
