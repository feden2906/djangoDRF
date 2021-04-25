from rest_framework.serializers import ModelSerializer

from .models import OfficeModel


class OfficeSerializer(ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'                         # ('name', 'city') або []  - виводимо лише обраны поля
