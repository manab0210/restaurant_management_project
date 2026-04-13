from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class LoyaltyProgram(models.Model):
    name-models.CharField(max_length=50,unique=True,help_text="The name of the loyalty tier (e.g., 'Silver Member')")
    points_required=models.PositiveIntegerField(unique=True,help_text="Maximum points required to reach this tier")
    discount_percentage=models.DecimalField(max_digits=5,decimal_place=2,validators=[MinValueValidator(0),MaxValueValidator(100)],help_text="Percentage discount (e.g., 5.00 for 5%)")
    description = models.TextField(blank=True,help_text="Brief explanation of the benefitd for this tier")
    class Meta:
        ordering=['points_required']
        verbose_name="Loyalty Program Tier"

    def __str__(self):
        return f"{self.name} ({self.points_required} +points)"