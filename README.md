# Задание

Необходимо было проверить поддерживается ли сайт с помощью числа просмотров и дат на странице. 


# Проверка сайта

1. Проверка существования сайта
2. Проверка всех дат на сайте и оценка времени прошедшего с послдней записи
3. Проверка посещяемости веб-сайта с помощью данных с siteworthtraffic.com

# Технологии

Использовался python 2.7 с помощью виртуализации в [Vagrant](https://www.vagrantup.com/) и python - пакеты : urllib, lxml, datefinder, argparse

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
