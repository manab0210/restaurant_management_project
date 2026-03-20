from django.db import db,models

# Create your models here.
class MenuCategory(models.Model):
    name=models.CharField(max_lenght=100, unique=True)

    def __str__(self);
    return self.name
    
    class Meta:
        verbose_name_plural="MenuCategories"