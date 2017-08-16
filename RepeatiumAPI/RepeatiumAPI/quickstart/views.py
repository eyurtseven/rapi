# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import PackageSerializer

from RepeatiumAPI.quickstart.models import Package
from RepeatiumAPI.quickstart.serializers import UserSerializer, GroupSerializer, PackageSerializer


class ListPackage(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        packages = [p.__dict__ for p in Package.objects.all()]
        serializer = PackageSerializer(data=packages, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageListAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

