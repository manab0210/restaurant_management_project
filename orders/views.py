from rest_framework.generic import RetriveAPIView
from rest_framework.permission import IsAuthenticated
from .models import Order
from .serializers import OrderSreializer

class OrderHistoryListView(RetriveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSreializer