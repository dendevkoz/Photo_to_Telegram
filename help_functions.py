import requests
import os
from urllib.parse import urlsplit, unquote
from os import path
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
    clear_link = unquote(link)
    split_link = urlsplit(clear_link)
    extension = path.splitext(split_link.path)[1]
    return extension


def get_response(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def posted_all(dir_name, time_sleep, telegram_chat_id, bot):
    for root_folder, folder, files in os.walk(dir_name):
        for file_name in files:
           image_path = os.path.join(f"{root_folder}", f"{file_name}")
            with open(image_path, "rb") as image_file:
                bot.send_photo(chat_id=telegram_chat_id, photo=image_file)
            sleep(time_sleep)
            

def posted_one(bot, image_path, telegram_chat_id):
    with open(image_path, "rb") as image_file:
        bot.send_photo(chat_id=telegram_chat_id, photo=image_file)


def posted_random_image(dir_name, telegram_chat_id, bot):
    pictures = os.listdir(dir_name)
    picture = random.choice(pictures)
    for root_folder, folder, files in os.walk(dir_name):
        image_path = os.path.join(f"{root_folder}", f"{picture}")
        with open(image_path, "rb") as image_file:
            bot.send_photo(chat_id=telegram_chat_id, photo=image_file)


def take_only_image(nasa_apod_url, payload, count):
    type_image = []
    response = get_response(nasa_apod_url, payload)
    for item in range(count):
        if response[item]["media_type"] == "image":
            type_image.append(response[item])
    return type_image


