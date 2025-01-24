from django.urls import(
    path,
    include
)
from django.contrib.auth.models import User
from rest_framework import (
    routers,
    serializers,
    viewsets
)

from app.serializers import UserSerializer


# # Serializers define the API representations
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=User
#         fields = ['url', 'username', 'email', 'is_staff']


# # ViewSets define the user behavoir
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way  of automatically determining the URL conf
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # Wire up our API using automatic URL routing
# # Additionally, we include login URLs for the brousable API
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api_auth/', include('rest_framework.urls', namespace = 'rest_framework'))
# ]
