from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    category_name=serializers.ReadOnlyField(source='category.name')
    class Meta:
        model=MenuItem
        fields=['id','title','price','category','category_name']