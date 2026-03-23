from rest_framework import generics
from rest_framework.permission import IsAuthenticated
from .models import Order
from .serializers import OrderSreializer

class OrderHistoryListView(generics.ListAPIView):
    serializer_class=OrderSreializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

    def resturant_status_view(request):
        open_time,close_time=get_todat_operating_hours()

        if open_time and close_time:
            status=f"We are open today from {open_time} to {close_time}!"
        else:
            status="Sory, we are closed today."