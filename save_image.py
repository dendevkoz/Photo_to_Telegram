import requests


def save_all_image(image_url, image_path, headers=None, params=None):
    response = requests.get(image_url, headers=headers, params=params)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)







    


