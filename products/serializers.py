from rest_framework import serializers
from .models import Note

class MenuItemSerializer(serializers.ModelSerializer):
    class __all__:
        model =MenuItem
        fields='__all__'