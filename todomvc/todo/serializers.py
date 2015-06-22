from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todo.models import Todo

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')



class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'completed', 'order')
