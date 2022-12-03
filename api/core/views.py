from django.shortcuts import render
from rest_framework import viewsets
from .models import BankAccount
from.serializers import UserSelializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User_bank.objects.all()
    serializer_class = UserSerializer