from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OfficeSerializer
from .models import OfficeModel


class MyApiView(APIView):
    def get(self, *args, **kwargs):
        filt = self.request.query_params.get('city', None)
        qs = OfficeModel.objects.all()
        if filt:
            qs = qs.filter(city=filt)
        serializer = OfficeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response('created', status=status.HTTP_201_CREATED)

    def patch(self, *args, **kwargs):
        key = self.request.query_params.get('id')
        office = OfficeModel.objects.get(pk=key)
        data = self.request.data
        serializer = OfficeSerializer(office, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response('updated', status=status.HTTP_200_OK)