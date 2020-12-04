from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coin(db.Model):
    '''
        Bu class veritabanı ile diğer yapı arasında arayüz görevi görür. Başka bir ifade ile veritabanı ve kod arasında iletişim protokolü vazifesi görür.

        @id: Veritabanındaki Coin tablosunun id kolonunu temsil eder.
        @symbol: Veritabanındaki Coin tablosunun symbol kolonunu temsil eder.
        @price: Veritabanındaki Coin tablosunun price kolonunu temsil eder.
        @timestamp: Veritabanındaki Coin tablosunun timestamp kolonunu temsil eder.

    '''
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        '''
            Veritabanı sorgusundan sonra gelecek cevabın nasıl görüneceğini belirler.

            <Coin id=1, symbol=ETHBTC, price=0.031465, timestamp=2020-12-04 12:25:52.304522>
        '''
        return f'<Coin id={self.id}, symbol={self.symbol}, price={self.price}, timestamp={self.timestamp}>'
