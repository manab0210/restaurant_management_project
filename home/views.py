from rest_framework import viewsets, permissions
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

    def get_permissions(self):
        if self.action in ['update','partial_update','destroy','create']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes=[permissions.AllowAny]
        return [permission() for permission in permission_classes]