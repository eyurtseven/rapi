from django.contrib.auth.models import User, Group
from rest_framework import serializers

from RepeatiumAPI.quickstart.models import Package, Plan


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'price']


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = [
            'id',
            'planName',
            'projectCount',
            'projectCountText',
            'deviceCount',
            'deviceCountText',
            'price',
            'priceText',
            'isYearly',
            'description',
        ]

