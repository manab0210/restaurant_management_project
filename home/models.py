from django.db import db,models

# Create your models here.
class MenuCategory(models.Model):
    # name=models.CharField(max_lenght=100, unique=True)
    is_featured = models.BooleanField(default=False)
    def __str__(self);
    return self.title
    
    # class Meta:
    #     verbose_name_plural="MenuCategories"