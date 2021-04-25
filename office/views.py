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


class ReadUpdate(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        office = OfficeModel.objects.get(pk=id)
        office.delete()
        return Response('ok', status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        try:
            id = kwargs.get('id')
            office = OfficeModel.objects.get(pk=id)
            serializer = OfficeSerializer(office, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response('Office not found', status=status.HTTP_400_BAD_REQUEST)

    def put(self, *args, **kwargs):
        id = kwargs.get('id')
        office = OfficeModel.objects.get(pk=id)
        data = self.request.data
        serializer = OfficeSerializer(instance=office, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response('updated', status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        office = OfficeModel.objects.get(pk=id)
        data = self.request.data
        serializer = OfficeSerializer(instance=office, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response('updated', status=status.HTTP_200_OK)

