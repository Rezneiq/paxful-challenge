from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated #, IsAdminUser
from rest_framework.response import Response
from transactions.models import Transaction
from django.db.models import Sum
from utils.conversor import RatesConversor


class StatisticApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]          # ,IsAdminUser] I removed this permission in order to avoid the "hardcoded token"

    def get(self, request):
        queryset = Transaction.objects.all()
        profit = queryset.aggregate(total_profit_btc=Sum('profit'))
        count = queryset.count()
        
        usd_rate = RatesConversor().convert_to_usd(profit['total_profit_btc'])
        profit['total_profit_usd'] = usd_rate
        
        statistics = {
            'total_transactions': count,
            'total_profit': profit
        }
        return Response(statistics)