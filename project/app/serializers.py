from django.contrib.auth.models import (
    User,
    Group,
    )
from rest_framework import serializers
    

# Serializers define the API representations
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ['url', 'username', 'email', 'is_staff']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        # field = "__all__"
        fields = ['url', 'name']