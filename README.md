## Giriş

Bu proje binance.com üzerindeki belirli Bitcoin değerlerini elde edip 5 dakikada bir PostgresSQL veritabanına ekleyen ve eklediği verileri API olarak dışarı açan iki kısımlı bir uygulamadır.

## Kurulum

> Bu proje Ubuntu dağıtımında geliştirilmiştir. Kurulum Ubuntu dağıtımına göre yapılmıştır.

__Kullanılan yapılar:__
  
  1. Veritabanı olarak PostgresSQL. Docker üzerinden kurulumu yapılmıştır.
  2. PostgresSQL ile Python arasındaki bağlantı için psycopg2
  3. Veritabanı işlemlerinde ORM olarak SQLAlchemy (flask_sqlalchemy eklentisi şeklinde.)
  4. Verileri API olarak açmak için Flask

---

__Docker Kurulumu__

  1. Öncelikle Docker' ı bilgisayara kuralım. [Link](https://docs.docker.com/engine/install/ubuntu/)
  2. [Bu](https://docs.docker.com/engine/install/linux-postinstall/) linkteki `Post-installation steps for Linux` adımlarını da yapmanızı tavsiye ederim. Yapmazsanız Docker' ı her çalıştırdığınızda `sudo` ile çalıştırmalısınız.
  3. Üçüncü bir adım olarak `docker-compose`' u kurmalısınız: `sudo apt-get install docker-compose`

  Kurulumları gerçekleştirdikten sonra şimdi PostgresSQL' i Docker üzerinden kullanabilirsiniz. Bunun için projenin `src/rosources` dizinindeki docker-compose dosyasını çalıştırmanız yeterlidir:

    docker-compose -f src/resources/docker-compose.yaml up -d
  
  Yukarıdaki komut ile PostgresSQL image' i inecek ve arkaplanda PostgresSQL çalışacak. 
  
  PostgresSQL arayüzüne `http://localhost:5431` üzerinden erişebilirsiniz.<br/> 
  Kullanıcı adı: `postgres`,
  Şifre: `sade123`,
  Veritabanı: `postgres`

---

__Python ve PostgresSQL ile python' ın haberleşmesi için gerekenler__

    sudo apt-get install libpq-dev
    pip install -r requirenments.txt

## Kullanılması

İki ayrı yapı şeklinde çalışmaktadır. İki ayrı terminal üzerinden çalıştırabilirsiniz.

Verileri 5dk'a kadar bir veritabanına eklemek için `add.py`.

API için `api.py` dosyasını çalıştırınız. (localhost:5000)
