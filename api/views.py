from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from items.models import Item
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,)


from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser

# Create your views here.
class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name','description']
    


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = "item_id"
	permission_classes = [IsAuthenticated, IsAdminUser]
    


