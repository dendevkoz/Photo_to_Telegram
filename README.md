# Photo_to_Telrgram

Данная программа позволяет скачивать фотографии и выкладывать их в Телеграм канал.

## Как установить 

Для начала вам необходимо выполнить несколько шагов:
- Зарегистрироваться на сайте [NASA](https://api.nasa.gov/) и сгенерировать токен.
- Cоздать бота в Telegram[(Создаем бот в телеграм)](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Создать канал в Telegram и назначить бота Администратором.
  
```
[Python3](https://www.python.org/downloads/) должен быть уже установлен.
```
Потом создаём виртуальное окружение
```
python -m venv venv
Путь до корневой папки venv/scripts/activate
```
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как работает
- Для начала нужно создать файл `.env` и записать в него настройки:
    - NASA_KEY = "Ваш API ключ NASA"
    - TELEGRAM_TOKEN = "Ваш Телеграм токен"
    - CHAT_ID="ID вашего чата"
    - POST_TIME="Время задержки между постами"
    
- Для скачивания фотографий с сайта NASA используем fetch_nasa.py:
   - Нужно выбрать опеределенный аргумент:
        - -a (--apod)  -  Загружает изображения APOD
          ```
          python fetch_nasa.py -a
          ```
          - -c (--count)  -  Сколько изображений скачать? (По умолчанию : 50)
          ```
          python fetch_nasa.py -a -c 10
          ```
        - -e (--epic)  -  Загружает изображения EPIC
          ```
          python fetch_nasa.py -e
          ```

- Для скачивания фотографий с сайта SPACEX используем fetch_spacex_last_launch.py:
  - Нужно выбрать опеределенный аргумент:
     - -s (--spacex)  -  Загружает изображения SpaseX
      ```
        python fetch_spacex_last_launch.py -s
      ```
      или
      - -l LAUNCH_ID (--launch_id LAUNCH_ID)  -  Загружает изображения определенного запуска
      ```
        python fetch_spacex_last_launch.py -s -l "launc_id"
      ```
      
      Вместо "launch_id" можно вставить свой id запуска. По умолчанию "5eb87d47ffd86e000604b38a"

  
- Что бы выложить изображения в телеграм:
  ```
    python main.py
  ```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


