import requests
import json

# import config
from config import liveEvent, eventMatch
from utils import get_event_details, get_event_markets,get_event_selections


def savefile(jsonFile, jsonObj):
    with open(jsonFile, "w") as f:
        f.write(json.dumps(jsonObj))


# Request liveEvents
responseLiveEvents = requests.request(
    "GET", liveEvent.get("url"), headers=liveEvent.get("headers"), data=liveEvent.get("payload")
)
# response = response = requests.get(url, headers=headers)
responseLiveEvents_dict = json.loads(responseLiveEvents.text)
# save live event
savefile("data/01_LiveEvents.json", responseLiveEvents_dict)

for event in responseLiveEvents_dict["data"]:
    if event["categoryId"] == "1":
        print(50 * "#")
        print(f"{event}")
        fixturePopularity = event["fixturePopularity"]
        for eventId, val in fixturePopularity.items():
            eventConfig = eventMatch(eventId)
            print(eventConfig["url"])
            responseEvent = requests.get(eventConfig["url"], headers=eventConfig["headers"])
            responseEvent_dict = json.loads(responseEvent.text)
            # save event
            savefile(f"data/02_event_{eventId}_widgets.json", responseEvent_dict)
            # widgets
            widgets = responseEvent_dict["data"]["widgets"]
            for widget in widgets:
                widgetType = widget["type"]
                if widgetType == "Event":
                    eventObj = widget["data"]["data"]["scoreboard"]
                    savefile(f"data/02_event_{eventId}_{widgetType}.json", eventObj)
                    # Get participants, time and score.
                    get_event_details(eventObj)
                elif widgetType == "MarketList":
                    selectionsObj = widget["data"]["data"]["selections"]
                    savefile(
                        f"data/02_event_{eventId}_{widgetType}.json",
                        selectionsObj,
                    )
                    get_event_selections(selectionsObj)
