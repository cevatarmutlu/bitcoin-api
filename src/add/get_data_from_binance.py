import requests
from datetime import datetime

class CoinData:
  """
  CoinData class' ının görevi binance.com API' yına istek atarak belirli bitcoinlerin diğer bitcoinler cinsinden 
  değerlerini elde etmektir.

  Args:
      numeratorsCoins (Array): 
          Numerator pay demektir.
          Birbirleri cinsinden gösterilecek olan bitcoinlerin birim cinsinden gösterilecek coinleri tutmaktadır.
          Örnek: Dolar/TL gösterimindeki Dolar' ın bitcoin karşılığıdır.

      denominatorCoins (Array): 
          Denominator payda demektir.
          Birbirleri cinsinden gösterilecek olan bitcoinlerin değer olarak gösterilecek coinleri tutmaktadır.
          Örnek: Dolar/TL gösterimindeki TL' nin bitcoin karşılığıdır.
          
  """
  def __init__(self, numeratorCoins = ['ETH','BNB','XRP','BCH','LTC'], denominatorCoins = ['BTC']):
    '''
      Local Variables:

          numeratorCoins (Dizi): numerator' leri tutan değişken.
          denominatorCoins (Dizi): denominator' leri tutan değişken.
          url (String): Get isteği atılacak url.
          symbols (Dizi): API' ya atılacak bitcoin türlerini tutar. ETCBTC, BNBBTC gibi.

    '''

    self.numeratorCoins = numeratorCoins
    self.denominatorCoins = denominatorCoins
    self.url = 'https://api.binance.com/api/v3/ticker/price'
    self.symbols = self.generateSymbols()

  def generateSymbols(self):
    '''
      İstek atılacak symbol' ları oluşturan fonksiyondur.

      Args:
          Parametre almaz. `self.denominatorCoins` ile `self.numeratorCoins` dizileriyle beslenir.

      Return:
          sysmbols (Dizi): numarator ve denominator combinasyonlarını döndürür.

    '''

    symbols = []
    for denominator in self.denominatorCoins:
      symbols += [f'{numerator}{denominator}' for numerator in self.numeratorCoins]
    return symbols

  def get(self):
    '''
      `self.symbols` değişkenindeki bitcoin çiftlerinin değerlerini elde eder.

      Args:
          Parametre almaz.

      Return:
          datas (Dizi): API' dan gelen değerleri içinde barındırır.

    '''

    datas = []
    for symbol in self.symbols:
      req = requests.request(
        'get',
        self.url,
        params={'symbol': symbol}
      )
      res_json = req.json() # Cevap {'symbol': '...', 'price': '...'}
      form_res = self.dataConfig(res_json)
      datas.append(form_res)
    
    return datas

  def dataConfig(self, data):
    '''
      API' ya atılan istekleri belli formata sokan ve return eden fonksiyon.

      Args:
          data (JSON): Düzeltilecek veriyi tutan değişken. İçinde symbol ve price adında iki değer vardır.

      Return:
          Aldığı data değerini aşağıdaki format' a çevirerek return eder.
          {
            'symbol': data.get("symbol"),
            'price': data.get("price"),
            'timestamp': datetime.now(),
          }

    '''

    return {
      'symbol': data.get("symbol"),
      'price': data.get("price"),
      'timestamp': datetime.now(),
    }
