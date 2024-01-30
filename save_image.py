import requests
import os
from urllib.parse import urlsplit, unquote
from os import path


def save_all_image(image_url, image_path, headers=None, params=None):
    response = requests.get(image_url, headers=headers, params=params)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)


def create_directory():
    directory_path = os.path.join(os.getcwd(), 'images')
    os.path.exists(directory_path, exist_ok=True)
    return directory_path


def extension_file(link):
    clear_link = unquote(link)
    split_link = urlsplit(clear_link)
    extension = path.splitext(split_link.path)[1]
    return extension




    


