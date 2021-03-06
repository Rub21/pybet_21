import requests
import json
from time import sleep

# import config
from config import liveEvent, eventMatch
from utils import get_event_details, get_event_markets, get_event_selections, analyse_event
from send_message import telegram_bot_sendtext, checkIfMessageWasSent


def savefile(jsonFile, jsonObj):
    with open(jsonFile, "w") as f:
        f.write(json.dumps(jsonObj))


def init():

    # Request liveEvents
    responseLiveEvents = requests.request(
        "GET", liveEvent.get("url"), headers=liveEvent.get("headers"), data=liveEvent.get("payload")
    )
    # response = response = requests.get(url, headers=headers)
    responseLiveEvents_dict = json.loads(responseLiveEvents.text)
    # save live event
    savefile("data/01_LiveEvents.json", responseLiveEvents_dict)

    all_events_to_bet = []
    for event in responseLiveEvents_dict["data"]:
        if event["categoryId"] == "1":
            # print(50 * "#")
            # print(f"{event}")
            fixturePopularity = event["fixturePopularity"]
            for eventId, val in fixturePopularity.items():
                eventConfig = eventMatch(eventId)

                print(eventConfig["url"])

                responseEvent = requests.get(
                    eventConfig["url"], headers=eventConfig["headers"])
                responseEvent_dict = json.loads(responseEvent.text)

                # save event
                savefile(
                    f"data/02_event_{eventId}_widgets.json", responseEvent_dict)
                # widgets
                widgets = responseEvent_dict["data"]["widgets"]
                eventInfo = {}
                marketInfo = {}

                ####################################################
                # Cath error
                ###################################################
                try:
                    for widget in widgets:
                        widgetType = widget["type"]
                        # Check evet info
                        if widgetType == "Event":
                            eventObj = widget["data"]["data"]["scoreboard"]
                            savefile(
                                f"data/02_event_{eventId}_{widgetType}.json", eventObj)
                            # Get participants, time and score.
                            eventInfo = get_event_details(eventObj)
                        # Check Market
                        elif widgetType == "MarketList":
                            selectionsObj = widget["data"]["data"]["selections"]
                            savefile(
                                f"data/02_event_{eventId}_{widgetType}.json",
                                selectionsObj,
                            )
                            marketInfo = get_event_selections(selectionsObj)

                    eventInfo.update(marketInfo)
                    eventInfo['url'] = eventConfig["url"]

                    # Store all messsages
                    all_events_to_bet.append(eventInfo)

                    # # Analize
                    summary = analyse_event([eventInfo], 80)
                    # # Send message
                    if len(summary) > 0 and checkIfMessageWasSent(eventId):
                        print('########################')
                        print(f'{summary}')
                        print('########################')
                        telegram_bot_sendtext(summary)
                except:
                    print("An exception occurred")

    savefile("data/all_events_to_bet.json", all_events_to_bet)


while True:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    init()
    sleep(60)
