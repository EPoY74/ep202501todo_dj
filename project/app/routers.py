from rest_framework import routers
from .views import (
    UserViewSet,
    GroupViewSet,
    TasksViewSet
    )

# Routers provide an easy way  of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'tasks',TasksViewSet)