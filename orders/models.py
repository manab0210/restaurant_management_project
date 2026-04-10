from django.db import models

class OrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])
class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('processing','Processing'),
        ('shipped','Shipped'),
        ('cancelled','Cancelled'),
    ]
    status=models.CharField(max_length=20,choice=STATUS_CHOICES)
    created_at=models.DateTimeFeild(auto_now_add=True)

    objects=OrderManager()

    def __str__(self):
        return f"Order {self.id} - {self.status}"