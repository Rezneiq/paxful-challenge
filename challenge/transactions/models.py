from django.db import models
from wallets.models import Wallet
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Transaction(models.Model):
    from_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='from_wallet')
    to_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='to_wallet')
    profit = models.DecimalField(max_digits=15, decimal_places=5, default=0, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.from_wallet.address + ' to ' + self.to_wallet.address

def update_wallets_and_transaction(sender, instance, created, **kwargs):
    """ When a transaction is created, this will update
        the amounts on wallets."""
    if created:
        from_wallet = update_from_wallet(instance)
        to_wallet = update_to_wallet(instance)
        update_transaction_profit(instance, from_wallet, to_wallet)


post_save.connect(update_wallets_and_transaction, sender=Transaction)


def update_from_wallet(transaction_instance):
    print("haciendo update de from wallet", transaction_instance.from_wallet)
    from_wallet = Wallet.objects.get(address=transaction_instance.from_wallet)
    from_wallet.amount -= transaction_instance.amount
    from_wallet.save()
    return from_wallet


def update_to_wallet(transaction_instance):
    print("haciendo update de to wallet")
    to_wallet = Wallet.objects.get(address=transaction_instance.to_wallet)
    to_wallet.amount -= transaction_instance.amount
    to_wallet.save()
    return to_wallet


def update_transaction_profit(transaction_instance, from_wallet, to_wallet):
    if from_wallet.owner != to_wallet.owner:
        profit = 1.5 * float(transaction_instance.amount) / 100
        transaction_instance.profit = float(transaction_instance.amount) * 1.5 / 100
    else:
        transaction_instance.profit = 0
    transaction_instance.save()