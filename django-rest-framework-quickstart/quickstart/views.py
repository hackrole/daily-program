#!/usr/bin/env python
# encoding: utf-8

from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    u"""
    APi endpoiunt that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    u"""
    api endpoint that allows group to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
