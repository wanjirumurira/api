from rest_framework import viewsets

from .serializers import MyProfileSerializer
from .models import MyProfile


class MyProfileViewSet(viewsets.ModelViewSet):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileSerializer