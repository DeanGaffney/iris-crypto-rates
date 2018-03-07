#!/usr/bin/python

import requests, json
from coinmarketcap import Market

headers = {'Content-type': 'application/json', 
           'Accept': 'text/plain',
           'X-Auth-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJwcmluY2lwYWwiOiJINHNJQUFBQUFBQUFBSlZTdjBcL2JRQlIrRG9rb1FpcFFpVW9NZENuZGtDUEJtS21ndEJLeVFrV2FoVXF0THZiREhKenZ6TjBaa2dWbGdpRURxQzFTSlZaR1wvaE5ZK2dkVVpXQmw3dHAzaHVEQWdyakpmdmY1K1wvVjhmZ01WbzJFeDFvd0w0NmNpaTduMFRhcTVqQTJHbWVhMjYyY0dkWVEyUjN6TWdTMmF3TzN4U3VBRlVPS1JoVmZCRnR0bFZjRmtYRjF0YjJGb2F4ME5DMHJIZDR3Ym1pVzRwXC9TMmY4OGRLbzBQQkFwcTc2d0VvK3N3eGNKUVpkSTJsS3gzVXE0eFdvZkpZaGFvY051TnBrTzZRV2s1RTJZWU9vcVN0UVZHQVl5enpHNHFVdVZvTEV6Y21zMHNGOVVtMmxvQUwxSm1ETGw3bEtScG5YVjM3MnhLU3JBRCsxRHVwQjRkNnU2ZGdcL3FPeDE5V1FsQnFycVNaYThsRVJYeURPM0hpNzgxK1wvMzEwMm11VkFLaVQrYWVcL0tlWXpTOUM3K1BydlRWNjBGMXA0UFdTOWdOVTZLYm1aS3BnXC9hM1RLZjM1OStuRnljXC9obGhKUWQ0c1B6OXpIM1wvcTY1N3JKS1VxYVpWVU03SXRxOXNuc204cVdueVFkYjZQcE5ucVFDNlkrU0ZxTjdpWUtZNHBhMUVvTytMWXl0clFiMWI2MW1mYzI5VlZpVWNFbWlMXC9QTWJsbCtvR2hWXC9ldmp5Nk8zZjRsZ0JTcTdUR1JJbFU4V29FYVd0RkVmbkpcL01qdis4NnVjQkJqXC96ZjFtZmFkb1FBd0FBIiwic3ViIjoiYWRtaW4iLCJyb2xlcyI6WyJST0xFX1VTRVIiXSwiZXhwIjoxNTIwNDI2NDM4LCJpYXQiOjE1MjA0MjI4Mzh9.D-Ky6RgRQZrbfd4I5W642cV2ymJXwlWSIUG-rVWBo3o' }

agentData = {'name': 'crypto_agent'}

urlResp = requests.post('http://ec2-52-16-53-220.eu-west-1.compute.amazonaws.com:8080/iris/schema/getAgentUrl', data=json.dumps(agentData), headers=headers)

endpoint = urlResp.json()['url']

wanted_keys = ['price_usd', 'price_eur','name', 'percent_change_24h', 'rank']

def extract(data):
    return dict((k, data[k]) for k in wanted_keys if k in data)

coinmarketcap = Market()

crypto_currencies = coinmarketcap.ticker(limit=4, convert='EUR')

filterd_currencies = list(map(extract, crypto_currencies))

for currency in filterd_currencies:
    resp = requests.post(endpoint, data=json.dumps(currency), headers=headers)
    print resp.json()
