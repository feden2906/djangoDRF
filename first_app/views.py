from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OfficeSerializer


class MyApiView(APIView):
    def get(self, *args, **kwargs):
        return Response('Hi from myApiView')

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response('created')
