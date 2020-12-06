import threading
from src.add.add_postgres import Data
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
from src.add.get_data_from_binance import CoinData


class AddThread (threading.Thread):
  """
  AddThread class' ı belirli periyotlarda API' dan gelen verileri veritabanına ekler.
  """
  def __init__(self):
    threading.Thread.__init__(self)

    '''
      Local variables:
          app (Nesne), self.config (Nesne): 
              flask_sqlalchemy kullandığım için ve veritabanı işlemlerini gerçekleştirmek için 
              SQLAlchemy nesnesi bir Flask nesnesine ve Flask nesnesinin config['SQLALCHEMY_DATABASE_URI'] 
              değerinin atanmasına ihtiyaç duyuyor. Hızlıca bitirmek için üzerine düşünmedim.
          db (Nesne): Veritabanı işlemlerini gerçekleştirir.
          sleep_time (Integer): Periyot süresi. 5 dakika
    '''

    self.app = Flask(__name__)
    self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sade123@localhost:5432/postgres'
    self.db = SQLAlchemy(self.app)
    self.sleep_time = 60 * 5 # 5 dakika

  def run(self):
    '''
      Veritabanına verileri ekler ve Thread' i `sleep_time` kadar uyutur.

      Args:
          Parametre almaz.

      Return:
          Return değeri yoktur.

    '''

    while True:
      coins = CoinData().get()
      Data(self.db, coins).add()
      time.sleep(self.sleep_time)

if __name__ == "__main__":
    thread = AddThread()
    thread.start()