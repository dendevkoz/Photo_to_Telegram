import telegram
import os
from dotenv import dotenv_values
from time import sleep
from telegram.error import NetworkError


def send_to_bot():
    while True:
        for root_folder, folder, file in os.walk('images'):
            for file_name in file:
                image_path = os.path.join(f"{root_folder}", f"{file_name}")
                with open(image_path, "rb") as image_file:
                    photo = image_file.read()
                try:
                    bot = telegram.Bot(token=telegram_token)
                    bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                    sleep(14400)
                except NetworkError:
                    print("Ошибка подключения. Повторная попытка через 10 секунд...")
                    sleep(10)


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["TG_CHAT_ID"]
    send_to_bot()
