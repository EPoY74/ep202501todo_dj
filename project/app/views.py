from django.shortcuts import render
from django.contrib.auth.models import (
    User,
    Group,
    )
from rest_framework import viewsets

from app.serializers import (
    UserSerializer,
    GroupSerializer
    )

# Create your views here.


# ViewSets define the user behavoir
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
