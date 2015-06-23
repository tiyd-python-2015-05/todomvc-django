from rest_framework import serializers

from .models import TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'url', 'title', 'completed', 'order')
