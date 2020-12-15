from datetime import datetime, timedelta
from src.model.coin import Coin
from sqlalchemy import func

class Query:
  '''
      Gerekli PostgresSQL sorgularını yapar.

      Args:
          db (Nesne): Veritabanı işlemerini yapar.

    '''
  def __init__(self, db):
    
    self.db = db
  
  def all_coin_values(self):
    """
        Bütün bitcoin çiftlerinin değerlerini döndüren fonksiyon.

    Args:
        Argüman almaz.

    Return:
        (Dizi): Veritabanından gelen cevabı belli formata sokarak döndürür.
    """
    query = self.db.session.query(Coin).all()
    return [{'symbol': i.symbol,'price': i.price,'timestamp': i.timestamp} for i in query]
    
  def coin_values(self, symbol, time=15):
    '''
      Şuanki zaman ile belirli bir geçmiş dakika arasındaki bitcoinlerin değerlerini döndürür.

      Args:
          base (String): ETC/BTC değerinin pay kısmı olmaktadır.
          quote (String): ETC/BTC değerinin payda kısmı olmaktadır.
          minute (Integer): Şuanki zamandan kaç dakika geriye gidileceğini belirtir.

      Return:
          (Dizi): Veritabanından gelen cevabı belli formata sokarak döndürür.

    '''
    '''
    Local variables:
        beforeTime: Gerçerli zamandan kaç dakika geriye gidileceğini tutar.
        time: Şimdiki zamandan `beforeTime` geriye gidilmiş tarihi tutar.
        symbol: Hangi değere bakılacağını tutar. Default ETHBTC. Birim ETH' ın BTC türünden değeri.
        query: Veritabanı sorgusundan gelen cevabı tutar.
    '''

    try:
      time = float(time)
    except:
      time = 15

    beforeTime = timedelta(minutes=float(time))
    time = datetime.now() - beforeTime
    
    query = self.db.session.query(Coin).filter(Coin.symbol == symbol).filter(Coin.timestamp >= time).all()
    # Yukarıdaki sorgu: Coin tablosunda, symbol değeri `symbol` değişkenine eşit olan ve 
    # timestamp değeri ise `time` değişkeninden büyük olan satırları getir demektir.

    return [{'symbol': i.symbol,'price': i.price,'timestamp': i.timestamp} for i in query]

  def coin_avg(self, base='ETH', quote='BTC', hour=1):
    '''
      Şuanki zaman ile belirli bir geçmiş saat arasındaki coin karşılaştırılmasının ortalamasını döndürür.

      Args:
          base (String): ETC/BTC değerinin pay kısmı olmaktadır.
          quote (String): ETC/BTC değerinin payda kısmı olmaktadır.
          hour (Integer): Şuanki zamandan kaç saat geriye gidileceğini belirtir.

      Return:
          (Dict): Veritabanından gelen cevabı belli formata sokarak döndürür.

    '''
    '''
    Local variables:
        beforeTime: Gerçerli zamandan kaç saat geriye gidileceğini tutar.
        time: Şimdiki zamandan `beforeTime` geriye gidilmiş tarihi tutar.
        symbol: Hangi değere bakılacağını tutar. Default ETHBTC. Birim ETH' ın BTC türünden değeri.
        query: Veritabanı sorgusundan gelen cevabı tutar.
    '''

    beforeTime = timedelta(hours=hour)
    time = datetime.now() - beforeTime
    symbol = f'{base}{quote}'

    query = self.db.session.query(func.avg(Coin.price)).filter(Coin.symbol == symbol).filter(Coin.timestamp >= time).all()
    # Yukarıdaki sorgu: Coin tablosunda, symbol değeri `symbol` değişkenine eşit olan ve 
    # timestamp değeri ise `time` değişkeninden büyük olan satırların
    # price kolonlarının ortalamasını al demektir.

    return {
      'symbol': 'ETCBTC',
      'hour': '1',
      'avg': query[0][0],
    }
