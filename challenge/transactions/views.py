from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from wallets.models import Wallet
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction


class TransactionsApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer
    def get(self, request, format=None):
        queryset = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            from_wallet = get_wallet_instance(serializer.validated_data.get('from_wallet'))
            to_wallet = get_wallet_instance(serializer.validated_data.get('to_wallet'))
            amount = serializer.validated_data.get('amount')
            if not wallet_has_enough_amount(from_wallet, amount):
                return Response({
                    'error': "The wallet dosn't have enought money."
                }, status=status.HTTP_400_BAD_REQUEST)

            transaction = Transaction.objects.create(from_wallet=from_wallet, 
                                                     to_wallet=to_wallet, 
                                                     amount=amount, 
                                                     user=request.user
                                                     )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def wallet_has_enough_amount(wallet_instance, amount):
    print(amount, wallet_instance.amount, amount > wallet_instance.amount)
    if amount > wallet_instance.amount:
        return False
    return True

def get_wallet_instance(address):
    return Wallet.objects.get(address=address)