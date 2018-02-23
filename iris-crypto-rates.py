import requests
import from coinmarketcap import Market

coinmarketcap = Market()

crypto_currencies = coinmarketcap.ticker(limit=3, convert='EUR')
