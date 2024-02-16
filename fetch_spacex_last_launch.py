import requests
import os
from save_image import save_all_image, create_directory
import logging
import argparse


def fetch_spacex_last_launch():
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if 'error' in data:
        raise requests.exceptions.HTTPError(data['error'])
    else:
        image = data["links"]["flickr"]["original"]
        for image_number, image_url in enumerate(image):
            image_path = os.path.join(create_directory(dir_name), f"spacex_{image_number}.jpg")
            try:
                save_all_image(image_url, image_path)
            except requests.exceptions.HTTPError as error:
                logging.error("Не удалось сохранить изображение с сайта SpaceX:\n{0}".format(error))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Загрузка изображений с последнего запуска SpaceX"
    )
    parser.add_argument(
        "-s",
        "--spacex",
        help="Загружает изображения SpaseX",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--launch_id",
        type=str,
        help="Введите id запуска(По умолчанию : 5eb87d47ffd86e000604b38a",
        default="5eb87d47ffd86e000604b38a"
    )
    parser.add_argument(
        "-d",
        "--dir_name",
        type=str,
        help="Имя директории (По умолчанию : images)",
        default="images"
    )

    args = parser.parse_args()
    if args.spacex:
        try:
            dir_name = args.dir_name
            launch_id = args.launch_id
            fetch_spacex_last_launch()
        except requests.exceptions.HTTPError as error:
            logging.error("Невозможно получить данные с сайта SPACEX:\n{0}".format(error))
