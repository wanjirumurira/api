from rest_framework import serializers
from .models import MyProfile

class MyProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyProfile
        fields = '__all__'