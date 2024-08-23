from django.shortcuts import render
from rest_framework import viewsets
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer