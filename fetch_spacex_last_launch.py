import requests
import os
from save_image import save_all_image, create_directory


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    for description in data:
        if description["id"] == launch_id:
            image = description["links"]["flickr"]["original"]
            for image_number, image_url in enumerate(image):
                image_path = os.path.join(create_directory(), f"spacex_{image_number}.jpg")
                try:
                    save_all_image(image_url, image_path)
                except requests.exceptions.HTTPError as error:
                    logging.error("Не удалось сохранить изображение с сайта SpaceX:\n{0}".format(error))



if __name__ == "__main__":
    launch_id = "5eb87d47ffd86e000604b38a"
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        logging.error("Невозможно получить данные с сайта SPACEX:\n{0}".format(error))
