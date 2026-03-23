from rest_framework import generics
from rest_framework.permission import IsAuthenticated
from .models import Order
from .serializers import OrderSreializer

class OrderHistoryListView(generics.ListAPIView):
    serializer_class=OrderSreializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')