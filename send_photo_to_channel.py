import telegram
from dotenv import dotenv_values
from time import sleep
from telegram.error import NetworkError
import argparse
from help_functions import post_all, post_random_image, open_and_post


def send_to_bot(dir_name, time_sleep, image_path, path_to_random_image, bot):
    try:
        if image_path is not None:
            open_and_post(image_path, telegram_chat_id, bot)
        else:
            if path_to_random_image is not None:
                post_random_image(path_to_random_image, telegram_chat_id, bot)
            else:
                post_all(dir_name, time_sleep, telegram_chat_id, bot)
    except NetworkError:
        print("Ошибка подключения. Повторная попытка через 10 секунд...")
        sleep(10)


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["TG_CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)
    parser = argparse.ArgumentParser(
        description="Загрузка изображений в Телеграм"
    )
    parser.add_argument(
        "-d",
        "--dir_name",
        type=str,
        help="Имя директории откуда будут загружаться картинки (По умолчанию : images)",
        default="images",
    )
    parser.add_argument(
        "-t",
        "--time_sleep",
        type=int,
        help="""Время через которое происходят публикации
             (По умолчанию : 14400, число вводится в секундах : 
             Пример - 4 часа = 240 минут или 14400 секунд)""",
        default=14400,
    )
    parser.add_argument(
        "-p",
        "--image_path",
        type=str,
        help="Путь до картинки (Пример: images/nasa_apod1.jpg",
        default=None,
    )
    parser.add_argument(
        "-r",
        "--path_to_random_image",
        type=str,
        help="Путь до папки из которой будет взята рандомная картинка",
        default=None
    )
    args = parser.parse_args()
    dir_name = args.dir_name
    time_sleep = args.time_sleep
    image_path = args.image_path
    path_to_random_image = args.path_to_random_image
    send_to_bot(dir_name, time_sleep, image_path, path_to_random_image, bot)
