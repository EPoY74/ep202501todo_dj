from django.contrib.auth.models import (
    User,
    Group,
    )
from app.models import Task
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


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Task
        fields=['autor', 'create_at', 'shot_task_deskriptions', 
                'task_descriptions', 'due_time', 'сompleted_date', 
                'is_done']
    