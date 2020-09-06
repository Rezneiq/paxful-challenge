from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from wallets.models import Wallet
from wallets.serializers import WalletSerializer
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
import string
import random
import json
from utils.conversor import RatesConversor


class WalletTransactionsApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer
    
    def get(self, request, address):
        wallet = Wallet.objects.get(address=address)
        queryset = Transaction.objects.filter(from_wallet=wallet.id)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


class WalletApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletSerializer

    def get(self, request, address=None):
        if address:
            wallet = Wallet.objects.get(address=address)
            if wallet:
                serializer = WalletSerializer(wallet)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({
                'error': 'Wallet not found.'
            }, status=status.HTTP_404_NOT_FOUND)


class WalletsApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletSerializer
    
    def get(self, request, format=None):
        queryset = Wallet.objects.filter(owner=request.user)
        serializer = WalletSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_wallets = Wallet.objects.filter(owner=request.user).count()
        if user_wallets >= 10:
            return Response({
                'error': 'A user cannot have more than 10 wallets.'
            }, status=status.HTTP_400_BAD_REQUEST)

        address = generate_wallet_address()
        wallet = Wallet.objects.create(address=address, owner=request.user)
        serializer = WalletSerializer(wallet, data=request.data)
        if (serializer.is_valid()):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def generate_wallet_address():
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(characters) for _ in range(32)])
