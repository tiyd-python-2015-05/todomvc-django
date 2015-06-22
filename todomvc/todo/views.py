from django.shortcuts import render
from todomvc.todo.models import Todo
from rest_framework import viewsets
from todomvc.todo import serializers

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    pass