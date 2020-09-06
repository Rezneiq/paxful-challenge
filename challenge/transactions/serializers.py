from rest_framework import serializers
from transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'from_wallet', 'to_wallet', 'amount', 'user']
        # fields = '__all__'
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }