# Задание

Необходимо было проверить поддерживается ли сайт с помощью числа просмотров и дат на странице. 

Выполнил: Криницын А.В ИУ8-44

# Проверка сайта

1. Проверка существования сайта
2. Проверка делегирования домена
3. Проверка данных всех поддоменов
4. Проверка всех дат на сайте и оценка времени прошедшего с последней записи
5. Проверка посещяемости веб-сайта с помощью данных с каталога siteworthtraffic.com
6. Сравнение всей полученой информации 

# Технологии

Использовался python 2.7 с помощью виртуализации в [Vagrant](https://www.vagrantup.com/) и python - пакеты : urllib, lxml, datefinder, argparse, dnslib, subbrute, knock, pywhois 

# Тесты 

Было протестированно несколько сайтов:

1. [yandex.ru](http://yandex.ru) - Поддерживается
2. [forte-it.ru](http://forte-it.ru) - Возможно поддерживается
3. [sergeev-vf](http://sergeev-vf).ru - Возможно поддерживается
4. [ruspred.ru](http://ruspred.ru) - Не поддерживается

Видно что тесты были пройдены без ошибок

# Скриншоты 

![Terminal](https://raw.githubusercontent.com/i14564/Practice-2016/master/screenshots/command-line.png)
![Tests](https://raw.githubusercontent.com/i14564/Practice-2016/master/screenshots/tests.png)
