from django.shortcuts import render
from rest_framework import viewsets
from todo.models import *
from todo.serializer import *

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
