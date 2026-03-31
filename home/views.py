# from rest_framework.generics import ListAPIView
# from .models import MenuItem
# from .serializers import MenuItemSerializer
# class MenuCategoryListView(ListAPIView):
#     serializer_class=MenuItemSerializer

#     def get_queryset(self):
#         return MenuItem.object.filter(is_featured=True)
from django.shortcuts import render
from .models import DailySpecial

def home(request):
    context={
        'featured_special':DailySpecial.get_random_special()
        
    }
    return render(request,'home/index.html',context)