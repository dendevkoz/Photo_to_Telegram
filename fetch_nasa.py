import os
import requests
import datetime
from dotenv import dotenv_values
from save_image import save_all_image, create_directory, define_extension
import logging
import argparse
  

def fetch_nasa_apod(nasa_api_key):
    nasa_apod_url = f"https://api.nasa.gov/planetary/apod"
    payload = {
        "count": count,
        "api_key": nasa_api_key,
    }
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    data = response.json()
    urls_images = [description["url"] for description in data]  
    for image_number, image_url in enumerate(urls_images):
        extension = str(define_extension(image_url))
        image_path = os.path.join(create_directory(), f"nasa_apod{image_number}{extension}")
        try:
            save_all_image(image_url, image_path)
        except requests.exceptions.HTTPError as error:
            logging.error("Не удалось сохранить изображение с сайта NASA-APOD:\n{0}".format(error))  


def fetch_nasa_epic(nasa_api_key):
    nasa_epic_url = f"https://api.nasa.gov/EPIC/api/natural/all"
    payload = {
        "api_key": nasa_api_key,
    }
    date_response = requests.get(nasa_epic_url, params=payload)
    date_response.raise_for_status()
    data = date_response.json()
    last_date = datetime.date.fromisoformat(data[0]["date"])
    last_date_formatted = last_date.strftime("%Y/%m/%d")
    last_date_respone = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{last_date}", params=payload)
    last_date_image = last_date_respone.json()
    picture_names = [description["image"] for description in last_date_image]
    for name in picture_names:
        response = requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{last_date_formatted}/png/{name}.png", params=payload)
        extension = ".png"
        picture_date = datetime.datetime.now().timestamp()
        image_path = os.path.join(create_directory(), f"nasa_epic_{int(picture_date)}{extension}")
        try:
            save_all_image(response.url, image_path)
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
    args = parser.parse_args()
    if args.apod:
      try:
          count = args.count
          fetch_nasa_apod(nasa_api_key)
      except requests.exceptions.HTTPError as error:
          exit("Невозможно получить данные с сайта NASA EPIC или NASA APOD:\n{0}".format(error))
    if args.epic:
      try:
          fetch_nasa_epic(nasa_api_key)
      except requests.exceptions.HTTPError as error:
          exit("Невозможно получить данные с сайта NASA EPIC или NASA APOD:\n{0}".format(error))
