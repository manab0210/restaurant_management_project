from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Coupon(models.Model):
    code=models.CharField(max_lenght=50,unique=True)
    discount_percentage=models.DecimalField(
        max_digits=3,
        decima;_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(1)]
    )
    is_active=models.BooleanField(default=True)
    valid_form=models.DateField()
    valid_until=models.DateField()
    
    def __str__(self):
        return f"{self.code}({self.discount_percentage*100}%)"