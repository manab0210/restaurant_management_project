from django.db import models

class OrderStatus(models.Model):
    name=models.CharField(max_lenght=50,unique=True)
    status =models.FroeginKey(
        'OrderStatus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    def __str__(self):
        return self.name
        return f"Order #{self.id} - {self.status}"
    class Meta:
        verbose_name_plural="Order Statuses"