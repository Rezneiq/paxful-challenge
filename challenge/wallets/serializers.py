from rest_framework import serializers
from wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    amount_usd = serializers.ReadOnlyField()
    class Meta:
        model = Wallet
        fields = ['id', 'address', 'amount', 'amount_usd', 'owner']
        extra_kwargs = {
            'address': {
                'read_only': True
            },
            'amount': {
                'read_only': True
            },
            'owner': {
                'read_only': True
            }
        }