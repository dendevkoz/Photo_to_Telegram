import telegram
import os
from dotenv import dotenv_values
from time import sleep


def send_to_bot(bot, telegram_chat_id):
    try:
        while True:
            for root_folder, folder, file in os.walk('images'):
                for file_name in file:
                    image_path = f"{root_folder}/{file_name}"
                    with open(image_path, "rb") as image_file:
                        photo = image_file.read()
                    bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                    sleep(14400)
    except telegram.error.NetworkError:
        print(f"Ошибка подключения. Повторная попытка через 5 секунд...")
        telegram.error.RetryAfter(5)


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)
    send_to_bot(bot, telegram_chat_id)
