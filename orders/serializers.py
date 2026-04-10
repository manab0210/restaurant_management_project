from rest_framework import serializers
from .models import Order , OrderItem

class OrderItemSreializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')
    class Meta:
        model=OrderItem
        fields=['id','product','product_name','quantity','price']
class OrderSreializer(serializers.ModelSerializer):
    items=OrderItemSreializer(many=True,read_only=True)
    customer_email=serializers.ReadOnlyField(source='customer.email')
    class Meta:
        modle=Order
        fields=['id','customer','customer_name','items','total_price','created_at','is_paid']