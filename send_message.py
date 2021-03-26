import time
import requests
from telegram import Bot
import json
bot_token = '1771669981:AAFTLnIoPGvGmpsdIHt4kGO1fGJnmWZa4ng'
bot_chatID = '-415040970'


def telegram_bot_sendtext(bot_message):

    # send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text="{bot_message}"'
    # print(send_text)
    # # https://api.telegram.org/bot1771669981:AAFTLnIoPGvGmpsdIHt4kGO1fGJnmWZa4ng/getUpdates
    # response = requests.get(send_text)
    # print(response.text)
    bot = Bot(bot_token)
    bot.send_message(bot_chatID, f'{bot_message}') #parse_mode='markdown'


# echo "[]" > messages.json
def checkIfMessageWasSent(eventId):
    message_file = 'messages.json'
    with open(message_file, "r") as f:
        events = json.load(f)

        if eventId in events:
            return False
        else:
            events.append(eventId)
            with open(message_file, "w") as f:
                f.write(json.dumps(events))
            return True
