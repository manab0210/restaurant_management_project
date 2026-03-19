from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'owner']
        # Set owner as read_only so it can't be changed via API input
        read_only_fields = ['owner', 'created_at']