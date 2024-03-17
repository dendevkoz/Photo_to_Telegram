# Photo_to_Telegram

Данная программа позволяет скачивать фотографии и выкладывать их в Телеграм канал.

## Как установить 

Для начала вам необходимо выполнить несколько шагов:
- Зарегистрироваться на сайте [NASA](https://api.nasa.gov/) и сгенерировать токен.
- Создать бота в Telegram[(Создаем бот в телеграм)](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)
- Создать канал в Telegram и назначить бота Администратором.
  
[Python3](https://www.python.org/downloads/) должен быть уже установлен.

Потом создаём виртуальное окружение
```python
python -m venv venv
```
Путь до корневой папки 
```python 
venv/scripts/activate
```

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```

## Как работает
- ### Для начала нужно создать файл `.env` и записать в него настройки:
    - NASA_KEY = "Ваш API ключ NASA"
    - TELEGRAM_TOKEN = "Ваш Телеграм токен"
    - TG_CHAT_ID="ID вашего чата"
    - POST_TIME="Время задержки между постами"
    
- ### Для скачивания фотографий с сайта NASA используем **fetch_nasa.py**:
   - Нужно выбрать определенный аргумент:
        - -a (--apod)  -  Загружает изображения APOD
          ```python
          python fetch_nasa.py -a
          ```
          - -c (--count)  -  Сколько изображений скачать? (По умолчанию: 50)
          ```python
          python fetch_nasa.py -a -c 10
          ```
        - -e (--epic)  -  Загружает изображения EPIC
          ```python
          python fetch_nasa.py -e
          ```
        - -d (--dir_name)  -  Имя директории (По умолчанию : images)
          ```python
          python fetch_nasa.py -e (или -a) -d (имя папки)
          ```

- ### Для скачивания фотографий с сайта SPACEX используем **fetch_spacex_last_launch.py**:
  - Нужно выбрать определенный аргумент:
     - -s (--spacex)  -  Загружает изображения SpaseX
      ```python
        python fetch_spacex_last_launch.py -s
      ```
      или
      - -l LAUNCH_ID (--launch_id LAUNCH_ID)  -  Загружает изображения определенного запуска
        
        Вместо "launch_id" можно вставить свой id запуска. По умолчанию "5eb87d47ffd86e000604b38a"

      ```python
        python fetch_spacex_last_launch.py -s -l "launc_id"
      ```
      - -d (--dir_name)  -  Имя директории (По умолчанию : images)
        ```python
        python fetch_spacex_last_launch.py -s -d (имя папки)
        ```

  
- ### Что бы выложить изображения в телеграм:
    - python main.py
    
       Публикует случайное изображение
      ```python
        python main.py
      ```
    - -d (--dir_name)  -  Имя директории (По умолчанию : images)
     
      Публикует все изображения из директории в бесконечном цикле 
      ```python
      python python main.py -d (имя папки)
      ```
    - -p (--image_path) - Путь до изображения (images/nasa_apod1.jpg)
     
      Публикует выбранное изображение
      ```python
      python main.py -p images/nasa_apod1.jpg
      ```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


