import os
import requests
import datetime
from dotenv import dotenv_values
from help_functions import save_all_image, create_directory, define_extension, get_response, take_only_images
import logging
import argparse
  

def fetch_nasa_apod(nasa_api_key, count, dir_name):
    nasa_apod_url = f"https://api.nasa.gov/planetary/apod"
    payload = {
        "count": count,
        "api_key": nasa_api_key,
    }
    image_only = take_only_images(nasa_apod_url, payload, count)
    get_image_url = [description["url"] for description in image_only]  
    for image_number, image_url in enumerate(get_image_url):
        extension = define_extension(image_url)
        image_path = os.path.join(create_directory(dir_name), f"nasa_apod{image_number}{extension}")
        try:
            save_all_image(image_url, image_path)
        except requests.exceptions.HTTPError as error:
            logging.error("Не удалось сохранить изображение с сайта NASA-APOD:\n{0}".format(error))  


def fetch_nasa_epic(nasa_api_key, dir_name):
    nasa_epic_url = f"https://api.nasa.gov/EPIC/api/natural/all"
    payload = {
        "api_key": nasa_api_key,
    }
    response = get_response(nasa_epic_url, payload)
    latest_date = datetime.date.fromisoformat(response[0]["date"])
    latest_date_formatted = latest_date.strftime("%Y/%m/%d")
    nasa_latest_date_url = f"https://api.nasa.gov/EPIC/api/natural/date/{latest_date}"
    latest_date_images = get_response(nasa_latest_date_url, payload)
    pictures_names = [description["image"] for description in latest_date_images]
    for name in picture_names:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{latest_date_formatted}/png/{name}.png"
        extension = ".png"
        picture_date = datetime.datetime.now().timestamp()
        image_path = os.path.join(create_directory(dir_name), f"nasa_epic_{picture_date}{extension}")
        try:
            save_all_image(image_url, image_path, params=payload)
        except requests.exceptions.HTTPError as error:
            logging.error("Не удалось сохранить изображение с сайта NASA-EPIC:\n{0}".format(error))


if __name__ == '__main__':
    nasa_api_key = dotenv_values(".env")["NASA_KEY"]
    parser = argparse.ArgumentParser(
        description="Загрузка APOD и Epic изображений с сайта NASA"
    )
    parser.add_argument(
        "-a",
        "--apod",
        help="Загружает изображения APOD",
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--epic",
        help="Загружает изображения EPIC",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        help="Сколько изображений скачать? (По умолчанию : 50)",
        default=50,
    )
    parser.add_argument(
      "-d",
      "--dir_name",
      type=str,
      help="Имя директории (По умолчанию : images)",
      default="images",
    )
    args = parser.parse_args()
    if args.apod:
        try:
            count = args.count
            dir_name = args.dir_name
            fetch_nasa_apod(nasa_api_key, count, dir_name)
        except requests.exceptions.HTTPError as error:
            exit("Невозможно получить данные с сайта NASA EPIC или NASA APOD:\n{0}".format(error))
    if args.epic:
        try:
            dir_name = args.dir_name
            fetch_nasa_epic(nasa_api_key, dir_name)
        except requests.exceptions.HTTPError as error:
            exit("Невозможно получить данные с сайта NASA EPIC или NASA APOD:\n{0}".format(error))
