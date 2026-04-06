from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

class TableList(generics.ListCreateAPIView):
    queryset=Table.objects.all()
    serializer_class = TableSerializer
class TableDetail(generics.RetrieveAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer