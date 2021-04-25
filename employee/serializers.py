from rest_framework.serializers import ModelSerializer

from employee.models import EmployeeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        # exclude = ('offices',)
        extra_kwargs = {'offices': {'read_only': True}}         # or 'write_only'

