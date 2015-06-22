from todo.models import ToDo
from todo.serializers import ToDoSerializer
from rest_framework import viewsets


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer