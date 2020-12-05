from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coin(db.Model):
    '''
        Veritabanı ve Python arasındaki iletişim protokolüdür. Coin tablosundaki satırları temsil eder.

        Variables:
            id: Veritabanındaki `Coin` tablosunun `id` kolonunu temsil eder.
            symbol: Veritabanındaki `Coin` tablosunun `symbol` kolonunu temsil eder.
            price: Veritabanındaki `Coin` tablosunun `price` kolonunu temsil eder.
            timestamp: Veritabanındaki `Coin` tablosunun `timestamp` kolonunu temsil eder.

    '''

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        '''
            Veritabanı sorgusundan sonra gelecek cevabın nasıl görüneceğini belirler.

            Args:
                Parametre almaz.

            Return:
                (String): Sorgudan gelen cevabı belli formata sokar.

        '''
        return f'<Coin id={self.id}, symbol={self.symbol}, price={self.price}, timestamp={self.timestamp}>'
