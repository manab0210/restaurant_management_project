from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuCategoryListView(ListAPIView):
    serializer_class=MenuItemSerializer

    def get_queryset(self):
        return MenuItem.object.filter(is_featured=True)