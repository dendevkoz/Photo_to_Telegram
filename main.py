import telegram
import os
from dotenv import dotenv_values
from time import sleep


def posting(bot, telegram_chat_id):
    while True:
        for root_folder, folder, file in os.walk('images'):
            for filename in file:
                image_path = f"{root_folder}/{filename}"
                with open(image_path, "rb") as image_file:
                    photo = image_file.read()
                bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                sleep(float(post_time))


if __name__ == "__main__":
    telegram_token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    telegram_chat_id = dotenv_values(".env")["CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)
    post_time = dotenv_values(".env")["POST_TIME"]
    posting(bot, telegram_chat_id)
