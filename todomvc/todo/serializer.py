from rest_framework import serializers
from todo.models import *

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'completed', 'order')
