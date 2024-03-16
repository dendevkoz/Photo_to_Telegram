import requests
import os
from urllib.parse import urlsplit, unquote
from os import path


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


def check_response(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def collect_images(dir_name):
    for root_folder, folder, files in os.walk(dir_name):
        for file_name in files:
            image_path = os.path.join(f"{root_folder}", f"{file_name}")
            with open(image_path, "rb") as image_file:
                photo = image_file.read()
    return photo
    


