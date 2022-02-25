from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.models import employee


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = employee
        fields = ['firstname','lastname','department']
