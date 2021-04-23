from django.urls import path
from .views import MyApiView, ReadUpdate

urlpatterns = [
    path('', MyApiView.as_view(), name='myApiView'),
    path('<int:id>', ReadUpdate.as_view(), name='ReadUpdate')
]
