# Пульт охраны банка "Сияние"
Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, 
но сможете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить

Проект запускается стандартным для Django образом командой в терминале:
```
python manage.py runserver 0.0.0.0:8000
```
### Пример работы проекта
Рассмотрим пример локального запуска проекта на Вашем компьютере.
После запуска проекта, как указано выше, Вы получаете доступ к проекту по ссылке:
```
127.0.0.1:8000
```
