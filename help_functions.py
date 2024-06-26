import requests
import os
from urllib.parse import urlsplit, unquote
from os import path
from telegram.error import NetworkError
from time import sleep
import random


def save_all_image(image_url, image_path, headers=None, params=None):
    response = requests.get(image_url, headers=headers, params=params)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)


def create_directory(dir_name):
    directory_path = os.path.join(os.getcwd(), dir_name)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def define_extension(link):
    decoded_link = unquote(link)
    parsed_link = urlsplit(decoded_link)
    extension = path.splitext(parsed_link.path)[1]
    return extension


def get_response(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def post_all_endlessly(dir_name, time_sleep, telegram_chat_id, bot):
    pictures_names_list = os.listdir(dir_name)
    while True:
        for picture_name in pictures_names_list:
            try:
                image_path = os.path.join(dir_name, picture_name)
                open_and_post(image_path, telegram_chat_id, bot)
                sleep(time_sleep)
            except NetworkError:
                print("Ошибка подключения. Повторная попытка через 10 секунд...")
                sleep(10)
        random.shuffle(pictures_names_list)
            

def post_random_image(path_to_random_image, telegram_chat_id, bot):
    pictures = os.listdir(path_to_random_image)
    picture = random.choice(pictures)
    image_path = os.path.join(path_to_random_image, picture)
    open_and_post(image_path, telegram_chat_id, bot)


def open_and_post(image_path, telegram_chat_id, bot):
    with open(image_path, "rb") as image_file:
        bot.send_photo(chat_id=telegram_chat_id, photo=image_file)




