import requests
import decimal

class RatesConversor:

    def __init__(self):
        self.rates = requests.get('https://bitpay.com/api/rates').json()

    def get_usd_rate(self):
        for currency in self.rates:
            if currency['code'] == 'USD':
                return currency['rate']

    def convert_to_usd(self, btc_amount):
        """ This method will return the converted
            amount from btc to usd """
        return decimal.Decimal(self.get_usd_rate()) * decimal.Decimal(btc_amount)