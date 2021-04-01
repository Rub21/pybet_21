import time
import requests
from telegram import Bot
import json

bot_token = "1771669981:AAFTLnIoPGvGmpsdIHt4kGO1fGJnmWZa4ng"
bot_chatID = "-415040970"
message_file = "messages.json"

with open(message_file, "w") as f:
    f.write(json.dumps([]))


def telegram_bot_sendtext(bot_message):

    # send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text="{bot_message}"'
    # print(send_text)
    # # https://api.telegram.org/bot1771669981:AAFTLnIoPGvGmpsdIHt4kGO1fGJnmWZa4ng/getUpdates
    # response = requests.get(send_text)
    # print(response.text)
    bot = Bot(bot_token)
    bot.send_message(bot_chatID, f"{bot_message}")  # parse_mode='markdown'


def telegram_bot_sendPhoto(bot_message, img):

    # send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text="{bot_message}"'
    # print(send_text)
    # # https://api.telegram.org/bot1771669981:AAFTLnIoPGvGmpsdIHt4kGO1fGJnmWZa4ng/getUpdates
    # response = requests.get(send_text)
    # print(response.text)
    bot = Bot(bot_token)
    bot.send_message(bot_chatID, f"{bot_message}")  # parse_mode='markdown'
    bot.send_photo(bot_chatID, photo=open(img, "rb"))


# echo "[]" > messages.json
def checkIfMessageWasSent(eventId, tiempo):
    event_id = f"{tiempo}_{eventId}"
    with open(message_file, "r") as f:
        events = json.load(f)
        if event_id in events:
            return False
        else:
            events.append(event_id)
            with open(message_file, "w") as f:
                f.write(json.dumps(events))
            return True
