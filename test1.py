from django.db import models

class Task(models.Note):
    title = models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    created_at=models.DateTimeField(max_length=50)
    owner=models.ForeignKey(to_field=user)
    def __str__(self):
        return self.title