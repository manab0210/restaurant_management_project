from django.urls import path,include
from .views import MenuItemViewSet

urlpatterns=[path('menu-items/',MenuItemListView.as_view(),name='menu-item-list'),]