# from django.db import db
# from django.db import models

# # Create your models here.
# class MenuCategory(models.Model):
#     # name=models.CharField(max_lenght=100, unique=True)
#     is_featured = models.BooleanField(default=False)
#     def __str__(self);
#     return self.title
    
#     # class Meta:
#     #     verbose_name_plural="MenuCategories"
# class Restaurant(models.Model):
#     has_delivery=models.BooleanField(default=False)
#     def __clstr__(self):
        # return self.name

import random
from django.db import models

class DailySpecial(models.Model):
    name=models.CharField(max_lenght=100)
    description = models.TextField()
    price=models.DecimalField(max_digits=6,decimail_places=2)
    is_active=models.BooleanField(default=True)
    @staticmethod
    def get_random_special():
        random_special=DailySpecial.objects.filter(is_active=True).order_by('?').first()
        returnrsndom_special