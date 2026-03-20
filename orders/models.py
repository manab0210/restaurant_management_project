from django.db import models

class OrderStatus(models.Model):
    name=models.CharField(max_lenght=50,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Order Statuses"