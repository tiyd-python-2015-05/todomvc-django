
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'url', 'title', 'completed', 'order')