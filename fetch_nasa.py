import os
import requests
import datetime
from dotenv import dotenv_values
from save_image import save_all_image
from urllib.parse import urlsplit, unquote
from os import path


def file_extension(link):
  link = unquote(link)
  link_split = urlsplit(link)
  extension = path.splitext(link_split.path)[1]
  return extension
  

def fetch_nasa_apod(nasa_api_key):
    nasa_apod_url = f"https://api.nasa.gov/planetary/apod"
    image=[]
    payload = {
        "count": 5,
        "api_key": nasa_api_key,
    }
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    data = response.json()
    directory = "images/nasa_apod"
    os.makedirs(directory, exist_ok=True)
    for item in data:
        image.append(item["url"])
    for image_number, image_url in enumerate(image):
        extension = str(file_extension(image_url))
        image_path = f"{directory}/nasa_apod{image_number}{extension}"
        try:
            save_all_image(image_url, image_path)
        except requests.exceptions.HTTPError as error:
            logging.error("Не удалось сохранить изображение с сайта NASA-APOD:\n{0}".format(error))  


def fetch_nasa_epic(nasa_api_key):
    nasa_epic_url = f"https://api.nasa.gov/EPIC/api/natural/all"
    image = []
    payload = {
        "api_key": nasa_api_key,
    }
    date_response = requests.get(nasa_epic_url, params=payload)
    date_response.raise_for_status()
    data = date_response.json()
    directory = "images/nasa_epic"
    os.makedirs(directory, exist_ok=True)
    last_date = datetime.date.fromisoformat(data[0]["date"])
    last_date_formatted = last_date.strftime("%Y/%m/%d")
    last_date_respone = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{last_date}",     params=payload)
    last_date_image = last_date_respone.json()
    for item in last_date_image:
        image.append(item["image"])
    for item in image:
        response = requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{last_date_formatted}/png/{item + '.png'}", params=payload)
        extension = ".png"
        image_path = f"{directory}/nasa_epic_{item[-4:]}{extension}"
        try:
            save_all_image(response.url, image_path)
        except requests.exceptions.HTTPError as error:
            logging.error("Не удалось сохранить изображение с сайта NASA-EPIC:\n{0}".format(error))



if __name__ == '__main__':
    nasa_api_key = dotenv_values(".env")["NASA_KEY"]
    try:
        fetch_nasa_epic(nasa_api_key)
        fetch_nasa_apod(nasa_api_key)
    except requests.exceptions.HTTPError as error:
        exit("Невозможно получить данные с сайта NASA EPIC или NASA APOD:\n{0}".format(error))
