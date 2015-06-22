from rest_framework import serializers
from todomvc.todo.models import Todo


class TodoSerializer(serializers.HyperModelSerializer):
    class Meta:
        model = Todo
        fields = ('completed', 'title', 'order')


