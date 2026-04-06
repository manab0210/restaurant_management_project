from django.db import models
from django.db.models import Count

class MenuItemManager(models.Manager):
    def get_top_selling_items(self,num_items=5):
        return self.get_queryset().annotate(
            total_sold=Count('orderitem')
        ).order_status('-total_sold')[:num_items]
class MenuItem(models.Model):
    name=models.CharField(max_lenght=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    objects=MenuItemManager()

    def __str__(self):
        return self.name