import requests
from datetime import datetime

class CoinData:
  """
  CoinData class' ının görevi binance.com API' yına istek atarak bitcoinlerin bitcoinler cinsinden
  değerlerini elde etmektir.
       
  """
  def __init__(self):
    '''
      Local Variables:

          url (String): Get isteği atılacak url.

    '''

    self.url = 'https://api.binance.com/api/v3/ticker/price'

  def get(self):
    '''
      `self.symbols` değişkenindeki bitcoin çiftlerinin değerlerini elde eder.

      Args:
          Parametre almaz.

      Return:
          datas (Dizi): API' dan gelen değerleri içinde barındırır.

    '''

    req = requests.request(
      'get',
      self.url,
    )
    datas = req.json() # Cevap [{'symbol': '...', 'price': '...'}, ....]
    
    print("Symbol çiftlerinin değerlerini çekme işlemi başarılı. Boyut: ", len(datas))
    return datas