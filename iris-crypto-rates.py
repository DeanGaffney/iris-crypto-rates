#!/usr/bin/python

import requests, json
from coinmarketcap import Market

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

agentData = {'name': 'crypto_agent'}

urlResp = requests.post('http://ec2-52-16-53-220.eu-west-1.compute.amazonaws.com:8080/iris/schema/getAgentUrl', data=json.dumps(agentData), headers=headers)

endpoint = urlResp.json()['url']

wanted_keys = ['price_usd', 'price_eur','name', 'percent_change_24h', 'rank']

def extract(data):
    return dict((k, data[k]) for k in wanted_keys if k in data)

coinmarketcap = Market()

crypto_currencies = coinmarketcap.ticker(limit=10, convert='EUR')

filterd_currencies = list(map(extract, crypto_currencies))

for currency in filterd_currencies:
    resp = requests.post(endpoint, data=json.dumps(currency), headers=headers)
    print resp.json()