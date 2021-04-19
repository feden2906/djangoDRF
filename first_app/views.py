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
            print(filt)
            qs = qs.filter()
        serializer = OfficeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response('created', status=status.HTTP_201_CREATED)
