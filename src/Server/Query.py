from datetime import datetime, timedelta
from src.Model_Coin import Coin
from sqlalchemy import func

class Query:
  def __init__(self, db):
    '''
      Query Class' ı PostgresSQL sorgusu yapan class.

      init parametreleri:
        @self.db: Nesne, Veritabanı işlemerini yapar.
    '''
    self.db = db
    
  def coin_values(self, numerator='ETH', denominator='BTC', minute=15):
    '''
      Şuanki zaman ile belirli bir geçmiş dakika arasındaki bitcoinlerin değerlerini döndürür.
      Birim @numerator' i @denominator cinsinden gösterir.

      parametreler:
        @numerator: String, ETC/BTC değerinin pay kısmı olmaktadır. İstendiği gibi ETH.
        @numerator: String, ETC/BTC değerinin payda kısmı olmaktadır. İstendiği gibi BTC.
        @minute: Integer, Şuanki zamandan kaç dakika geriye gidileceğini belirtir. Task' ta belirtildiği gibi 15 olarak ayarlandı.

      değişkenler:
        @beforeTime: Gerçerli zamandan kaç dakika geriye gidileceğini tutar
        @time: Şimdiki zamandan @beforeTime geriye gidilmiş tarihi tutar.
        @symbol: Hangi değere bakılacağını tutar. Default ETHBTC. Birim ETH' ın BTC türünden değeri.
        @query: Veritabanını sorgusundan gelen değerleri tutar. Sorgu Coin tablosunda, Coin.symbol değeri symbol olan
        Coin.timestamp değeri ise time' dan büyük olan bütün değerleri getirir.

      Fonksiyonda kullanılan Class' lar:
        Coin:
          
          Coin tablosundaki satırı temsil ediyor. Parametre olarak Coin tablosundaki bütün kolonları barındırır.
    '''

    beforeTime = timedelta(minutes=minute)
    time = datetime.now() - beforeTime
    symbol = f'{numerator}{denominator}'
    query = self.db.session.query(Coin).filter(Coin.symbol == symbol).filter(Coin.timestamp >= time).all()

    return [{'symbol': i.symbol,'price': i.price,'timestamp': i.timestamp} for i in query]

  def coin_avg(self, numerator='ETH', denominator='BTC', hour=1):
    '''
      Şuanki zaman ile belirli bir geçmiş saat arasındaki değerlerinin ortalamasını döndürür.
      Birim @numerator' i @denominator cinsinden gösterir.

      parametreler:
        @numerator: String, ETC/BTC değerinin pay kısmı olmaktadır. İstendiği gibi ETH.
        @numerator: String, ETC/BTC değerinin payda kısmı olmaktadır. İstendiği gibi BTC.
        @minute: Integer, Şuanki zamandan kaç dakika geriye gidileceğini belirtir. Task' ta belirtildiği gibi 15 olarak ayarlandı.

      
      değişkenler:
        @beforeTime: Gerçerli zamandan kaç dakika geriye gidileceğini tutar
        @time: Şimdiki zamandan @beforeTime geriye gidilmiş tarihi tutar.
        @symbol: Hangi değere bakılacağını tutar. Default ETHBTC. Birim ETH' ın BTC türünden değeri.
        @query: Veritabanını sorgusundan gelen değerleri tutar. Sorgu Coin tablosunda Coin.price değerlerinin 
        ortalamasını alarak ve Coin.symbol değeri symbol olan ve Coin.timestamp değeri ise time' dan büyük olan 
        bütün değerleri getirir.

      Fonksiyonda kullanılan Class' lar:
        Coin:
          
          Coin tablosundaki satırı temsil ediyor. Parametre olarak Coin tablosundaki bütün kolonları barındırır.
    '''

    beforeTime = timedelta(hours=hour)
    time = datetime.now() - beforeTime
    symbol = f'{numerator}{denominator}'
    query = self.db.session.query(func.avg(Coin.price)).filter(Coin.symbol == "ETHBTC").filter(Coin.timestamp >= time).all()
    return {
      'symbol': 'ETCBTC',
      'hour': '1',
      'avg': query[0][0],
    }
