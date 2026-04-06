from django.urls import path
from .views import TableList,TableDetail

urlpatterns=[
    path('api/tables/',TableList.as_view(),name='table-list'),
    path('api/tables/<int:pk>',TableDetail.as_view(),name='table-detail'),
]