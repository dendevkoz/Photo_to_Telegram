import telegram
from dotenv import dotenv_values
from time import sleep
from telegram.error import NetworkError
import argparse
from help_functions import posted_all, posted_one, posted_random_image



def send_to_bot(dir_name, time_sleep, image_path):
    try:
        bot = telegram.Bot(token=telegram_token)
        if image_path:
            posted_one(bot, image_path, telegram_chat_id)
        elif dir_name:
            posted_random_image(dir_name, telegram_chat_id, bot)
        else:
        posted_all(dir_name, time_sleep, telegram_chat_id, bot)
    except NetworkError:
        print("Ошибка подключения. Повторная попытка через 10 секунд...")
        sleep(10)


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["TG_CHAT_ID"]
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
        help="Время через которое происходят публикации (По умолчанию : 14400, число вводится в секундах : Пример - 4 часа = 240 минут или 14400 секунд)",
        default=14400,
    )
     parser.add_argument(
        "-p",
        "--image_path",
        type=str,
        help="Путь до картинки",
        default=None,
    )
    args = parser.parse_args()
    dir_name = args.dir_name
    time_sleep = args.time_sleep
    image_path = args.image_path
    send_to_bot(dir_name, time_sleep, image_path)
