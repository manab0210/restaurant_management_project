from django.db import models

# Create your models here.
# class Item(models.Model):
#     item_name = models.CharField(max_length=150)
#     item_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.item_name)

class NuteritionalInformation(models.Model):
    menu_item=models.OneToOneField('MenuItem',on_delete=models.CASCADE,related_name='nutrition')
    calories=models.IntegerField(help_text="Total calories per serving")
    protein_grams=models.DecimalField(max_digits=5,decimal_places=2,help_text="Protein content in grams")
    fat_grams=models.DecimalField(max_digits=5,decimal_places=2,help_text="Total carbohydrates in grams")
    def __str__(self):
        return f"Nutrition for {self.menu_item.name}({self.calories} kcal)"