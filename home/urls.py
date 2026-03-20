from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path('api/categories',MenuCategoryListView.as_view(),name='category_list')
]