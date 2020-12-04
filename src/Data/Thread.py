import threading
from src.Data.add_postgres import Data
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
from src.Data.get_data_from_binance import CoinData


class AddThread (threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

    '''
      AddThread class' ı belirli periyotlarda API' dan gelen verileri veritabanına ekler.

      class değişkenleri:
        @self.app, @self.config: Nesne, flask_sqlalchemy kullandığım için ve veritabanı işlemlerini gerçekleştirmek için SQLAlchemy nesnesi bir Flask nesnesine ve Flask nesnesinin config['SQLALCHEMY_DATABASE_URI'] değerinin atanmasına ihtiyaç duyuyor. Hızlıca bitirmek için üzerine düşünmedim.
        @self.db: Nesne, Veritabanı işlemlerini gerçekleştirir.
        @self.coins: Dizi, API' dan gelen velen verileri tutar.
        @self.sleep_time: Integer, Bu Thread' ın hangi aralıkta bir verileri veritabanına ekleyeceğini belirler. Default olarak 5dk
    '''

    self.app = Flask(__name__)
    self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sade123@localhost:5432/postgres'
    self.db = SQLAlchemy(self.app)
    self.coins = CoinData().get()
    self.sleep_time = 60 * 5

  def run(self):
    '''
      Bu Thread' ın yapacağı işlemi belirtir: Veritabanına veri ekleme ve Thread' i @self.sleep_time kadar uyutma.

      Fonksiyonda kullanılan Class' lar:
        
        Data(db, coins): 

          Veritabanına verileri ekler

          parametler:
            db: Nesne, Veritabanı işlemlerini yapmasını sağlar -> (@self.db)
            coins: Veritabanına ekleyeceği verileri tutar -> (@self.coins)
    '''

    while True:
      Data(self.db, self.coins).add()
      print('Veri ekleme başarılı')
      time.sleep(self.sleep_time)

if __name__ == "__main__":
    thread = AddThread()
    thread.start()