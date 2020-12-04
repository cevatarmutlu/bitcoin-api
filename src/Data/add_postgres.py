from src.Model_Coin import Coin

class Data:
  def __init__(self, db, coins):

    '''
      Uygun isim aklıma gelmeyen Data class' ının vazifesi PostgresSQL' e veri eklemektir.

      init parametreleri:
        @db: Nesne, Veritabanı işlemlerini yapmamızı sağlar.
        @coins: Dizi, API' dan gelen verileri tutar.
    '''

    self.db = db
    self.coins = coins
  
  def add(self):
    '''
      PostgresSQL' e verileri ekler.

      @self.coins içindeki verilerden Coin nesnesi oluşturur ve oluşturduğu nesneyi veritabanına ekler. Ekleme işlemi self.bd.session.commit() işlemi ile gerçekleşir.
      Coin nesnesi veritabanı ile haberleşmede kullanılan nesne. Veritabanında satıra karşılık gelen nesne de diyebiliriz.
    '''
    for coin in self.coins:
      row = Coin(
        symbol=coin.get('symbol'),
        price=coin.get('price'),
        timestamp=coin.get('timestamp')
      )
      self.db.session.add(row)
    self.db.session.commit()
  