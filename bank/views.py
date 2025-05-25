# from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, Account, Transfer
from .serializers import ClientSerializer, AccountSerializer, TransferSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer



