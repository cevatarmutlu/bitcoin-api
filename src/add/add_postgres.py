from src.model.coin import Coin
from datetime import datetime

class Data:
  """Uygun isim aklıma gelmeyen Data class' ının vazifesi PostgresSQL' e veri eklemektir.

  Args:
      db (Nesne): Veritabanı işlemlerini yapmamızı sağlar.
      coins (Dizi): API' dan gelen verileri tutar.

  """

  def __init__(self, db, coins):
    self.db = db
    self.coins = coins
  
  def add(self):
    '''
      PostgresSQL' e verileri ekler.

      Args:
          Parametre almaz

      Return:
          Return değeri yoktur.
          
    '''
    for i, coin in enumerate(self.coins):
      row = Coin(
        symbol=coin.get('symbol'),
        price=coin.get('price'),
        timestamp=datetime.now()
      )
      self.db.session.add(row)
    self.db.session.commit() # Ekleme işlemini gerçekleştirir.
    print("Veriler veritabanına eklendi\n")
  