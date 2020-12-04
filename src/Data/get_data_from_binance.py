import requests
from datetime import datetime

# # API sıralaması en eski ilk, en geç son
# api_key = 'NkUwlwYGsFq15TR8dsLNe7pxMQrR1QNb4L02a5CNOspuD3kEilHHQ6cTTCzBJCvO'
# api_secret_key = '4tiZiRWNdWtCq3wWMdigTC88lKooRYoHMrx3yNDau71R8odddpEFh84UPqwsDjYc'

# headers = {'X-MBX-APIKEY' : api_key}

class CoinData:
  def __init__(self, numeratorCoins = ['ETH','BNB','XRP','BCH','LTC'], denominatorCoins = ['BTC']):
    '''
      CoinData class' ı binance.com API' yına istek atarak belirli bitcoinlerin diğer bitcoinler cinsinden 
      değerlerini elde etme görevi olan class.

      init parametreleri: 
        @numeratorsCoins: Dizi, Bu parametre ETH/BTC karşılatırılmasındaki ilk kısımları tutan değişkendir. Numerator pay demektir. Default değeri ['ETH','BNB','XRP','BCH','LTC'].
        @denominatorCoins: Dizi, Bu parametre ETH/BTC karşılaştırılmasındaki ikinci kısımları tutan değişkendir. Denominator payda demektir. Default değeri ['BTC'].

      class değişkenleri:
        @numeratorCoins: Dizi, numerator' leri tutan değişken.
        @denominatorCoins: Dizi, denominator' leri tutan değişken.
        @url: String, Get isteği atılacak url
        @symbols: Dizi, Binance.com API' ına istekler ETHBTC şeklinde atılmaktadır. Bu değişken her Numerator ile her Denominator birleşimlerini tutan bir dizidir.
    '''

    self.numeratorCoins = numeratorCoins
    self.denominatorCoins = denominatorCoins
    self.url = 'https://api.binance.com/api/v3/ticker/price'
    self.symbols = self.generateSymbols()

  def generateSymbols(self):
    '''
      İstek atılacak symbol' ları oluşturan fonksiyondur.

      @self.denominatorCoins dizisindeki bütün elemanları self.numeratorCoins' deki bütün elemanlarla birleştirir.
    '''

    symbols = []
    for denominator in self.denominatorCoins:
      symbols += [f'{numerator}{denominator}' for numerator in self.numeratorCoins]
    return symbols

  def get(self):
    '''
      Belirtilen bütün coin karşılaştırmalarının değerlerini elde eden ve return eden fonksiyon.

      @self.symbols dizisindeki bütün elemanlar için API' ya istek atan ve gelen cevabı yerel @datas dizisine ekler.
    '''

    datas = []
    for symbol in self.symbols:
      req = requests.request(
        'get',
        self.url,
        params={'symbol': symbol}
      )
      datas.append(self.dataConfig(req.json()))
    
    return datas

  def dataConfig(self, data):
    '''
      API' ya atılan istekleri belli formata sokan ve return eden fonksiyon.

      parametreler:
        @data: JSON, Düzeltilecek veriyi tutan değişken. İçinde symbol ve price adında iki key değeri vardır.

      @data değişkenindeki symbol ve price değerlerini timestamp değeri ile beraber bir dictionary oluşturur.
    '''

    return {
      'symbol': data.get("symbol"),
      'price': data.get("price"),
      'timestamp': datetime.now(),
    }
