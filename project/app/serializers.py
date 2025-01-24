from django.contrib.auth.models import User
from rest_framework import serializers
    

# Serializers define the API representations
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ['url', 'username', 'email', 'is_staff']