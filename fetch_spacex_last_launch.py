import requests
import os
from save_image import save_all_image


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    for item in data:
        if item["id"] == "5eb87d47ffd86e000604b38a":
            image = item["links"]["flickr"]["original"]
            directory = "images/spacex_last_launch"
            os.makedirs(directory, exist_ok=True)
            for image_number, image_url in enumerate(image):
                image_path = os.path.join(directory, f"spacex_{image_number}.jpg")
                save_all_image(image_url, image_path)




if __name__ == "__main__":
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        logging.error("Невозможно получить данные с сайта SPACEX:\n{0}".format(error))
