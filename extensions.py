import json
import requests
from config import keys

class ConvertionExeptin(Exception):
    pass

class Convertor:
    @staticmethod
    def conver(quote: str, base:str, amount:str):
        if quote == base:
            raise ConvertionExeptin(f'не возможно перевести одинаковые валюты {base}. ')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeptin(f'не удалось обработать валюту {quote}. ')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeptin(f'не удалось обрабатать валюту {base}. ')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeptin(f'не удаёться обратить количество {amount}. ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base

