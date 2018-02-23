import requests, json
from coinmarketcap import Market

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
endpoint = ''
wanted_keys = ['price_usd', 'price_eur','name', 'percent_change_24h']

def extract(data):
    return dict((k, data[k]) for k in wanted_keys if k in data)

coinmarketcap = Market()

crypto_currencies = coinmarketcap.ticker(limit=3, convert='EUR')

filterd_currencies = list(map(extract, crypto_currencies))

for currency in filterd_currencies:
    print currency
    #requests.post(endpoint, data=json.dumps(currency), headers=headers)
