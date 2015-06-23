#from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from .serializers import TodoListSerializer
from .models import TodoList


class TodoListViewSet(viewsets.ModelViewSet):
    """
    List all todos
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
