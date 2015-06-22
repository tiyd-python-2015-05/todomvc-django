from django.shortcuts import render
from rest_framework import viewsets
from todo.serializers import TodoSerializer
from .models import Todo


# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.get.all()
    serializer_class = TodoSerializer