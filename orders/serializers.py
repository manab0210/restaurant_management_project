from rest_framework import serializers
from .models import Order , OrderItem

class OrderItemSreializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['menu_item_name','quantity','price']
class OrderSreializer(serializers.ModelSerializer):
    items=OrderItemSreializer(many=True,read_only=True)
    class Meta:
        modle=Order
        fields=['id','created_at','total_price','items']