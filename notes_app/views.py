from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing note instances.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This ensures users only see their own notes
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the owner to the currently logged-in user
        serializer.save(owner=self.request.user)