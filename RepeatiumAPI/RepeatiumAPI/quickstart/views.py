# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import PackageSerializer

from RepeatiumAPI.quickstart.models import Package, Plan
from RepeatiumAPI.quickstart.serializers import UserSerializer, GroupSerializer, PackageSerializer, PlanSerializer


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


class PlanListAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.all()
        plan_type = self.request.query_params.get('plan-type', None)
        if plan_type is not None:
            if plan_type == "yearly":
                queryset = queryset.filter(isYearly='True')
            elif plan_type == "monthly":
                queryset = queryset.filter(isYearly='False')
        return queryset


class PlanDetailAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

