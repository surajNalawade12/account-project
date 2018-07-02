# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from account.serializers import AccountSerializer, EmployeeSerializer, RegistrationSerializer, UserSerializer
from account.models import Account, Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('branch','accountType','accountNo')
    permission_classes = (IsAuthenticated,)


class EmployeeViewSet(viewsets.ModelViewSet):
        queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = RegistrationSerializer
        permission_classes = (AllowAny,)

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
        search_fields = ('username')
        permission_classes = (AllowAny,)
