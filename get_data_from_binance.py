import requests

base_endpoint = 'https://api.binance.com'
endpoint = '/api/v3/ticker/price'
coins = [
  'ETH',
  'BNB',
  'XRP',
  'BCH',
  'LTC'
]

req = requests.request(
  'get', 
  base_endpoint + endpoint, 
  params={'symbol': f'ETHBTC'}
)
print(req.json())