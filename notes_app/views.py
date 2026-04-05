from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemListView(APIView):
    def get(self,request):
        category_name=request.query_params.get('category')
        queryset = MenuItem.objects.all()
        if category_name:
            queryset=queryset.filter(category__name__iexact=category_name)
        serializer = MenuItemSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)