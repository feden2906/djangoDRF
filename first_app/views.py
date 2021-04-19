from rest_framework.views import APIView
from rest_framework.response import Response


class MyApiView(APIView):
    def get(self, *args, **kwargs):
        return Response('Hi from myApiView')
