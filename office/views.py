from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OfficeSerializer
from employee.serializers import EmployeeSerializer
from .models import OfficeModel


class OfficeListCreateView(APIView):
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
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('created', status=status.HTTP_201_CREATED)


class OfficeRetrieveView(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        get_object_or_404(OfficeModel, pk=id).delete()
        return Response('ok', status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        office = get_object_or_404(OfficeModel, pk=id)
        serializer = OfficeSerializer(office, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        id = kwargs.get('id')
        office = get_object_or_404(OfficeModel, pk=id)
        data = self.request.data
        serializer = OfficeSerializer(instance=office, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('updated', status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        office = get_object_or_404(OfficeModel, pk=id)
        data = self.request.data
        serializer = OfficeSerializer(instance=office, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('updated', status=status.HTTP_200_OK)


class OfficeEmployeeCreateView(APIView):
    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        office = get_object_or_404(OfficeModel, pk=pk)
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(offices_id=pk)               # <-----|  те саме
        serializer.save(offices=office)                # <-----|
        return Response(serializer.data)
