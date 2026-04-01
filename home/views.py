from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemIngredientSerializer
class MenuItemIngredientsView(RetrieveAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemIngredientsSerializer