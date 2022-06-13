import requests


url= 'https://api.coinbase.com/v2/prices/btc-usd/spot'

price = ((requests.get(url)).json())['data']
print(price)