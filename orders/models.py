from django.db import models
from django.conf import settings
from home.models import Product

class Order(models.Model):
    customer=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    total_price= models.DecimalField(max_digits=10,decimal_place=2)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_place=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"