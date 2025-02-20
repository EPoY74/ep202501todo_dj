from django.shortcuts import render
from django.contrib.auth.models import (
    User,
    Group,
    )
from rest_framework import (
    viewsets,
    permissions,
    )

from app.serializers import (
    UserSerializer,
    GroupSerializer,
    TasksSerializer
    )

from app.models import Task

# Create your views here.


# ViewSets define the user behavoir
class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoin that allows groups to be viewed or edited
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]