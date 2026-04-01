from rest_framework import serializers
from .models import MenuItem, Ingredient
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name','is_vegan']
class MenuItemIngredientsSerializer(serializers.ModelSerializer):
    ingredients=IngredientSerializer(many=True,read_only=True)
    class Meta:
        model=MenuItem
        fields=['id','name','ingredients']