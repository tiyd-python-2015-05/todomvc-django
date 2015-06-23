from django.shortcuts import render
from todo.models import Todo
from rest_framework import viewsets
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

