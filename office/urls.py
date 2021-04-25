from django.urls import path
from .views import OfficeRetrieveView, OfficeListCreateView

urlpatterns = [
    path('', OfficeListCreateView.as_view(), name='office_list_create'),
    path('/<int:id>', OfficeRetrieveView.as_view(), name='office_retrieve')
]
