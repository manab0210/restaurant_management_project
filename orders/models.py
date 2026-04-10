# from django.db import models

# class OrderStatus(models.Model):
#     name=models.CharField(max_lenght=50,unique=True)
#     status =models.FroeginKey(
#         'OrderStatus',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='orders'
#     )
#     def __str__(self):
#         return self.name
#         return f"Order #{self.id} - {self.status}"
#     class Meta:
#         verbose_name_plural="Order Statuses"
from django.db import models
from .utils import generate_coupon_code
class Coupon(models.Model):
    code=models.CharField(max_lenght20,unique=True)
    discount_amount=models.DecimalField(max_digits=10,decimal_places=2)
    def save(self,*srgs,**kwargs):
        if not self.code:
            self.code=generate_coupon_code()
        super().save(*args,**kwargs)
class Order(models.Model):
    def get_unique_item_names(self):
        item_names=self.orderitem_set.values_list('menu_item__name',flat=True)
        unique_name=list(set(item_names))
        return unique_names