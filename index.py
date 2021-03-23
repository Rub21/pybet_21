import requests
import json
# import config
from config import (liveEvent, eventMatch)


def savefile(jsonFile, jsonObj):
    with open(jsonFile, 'w') as f:
        f.write(json.dumps(jsonObj))


# Request liveEvents
responseLiveEvents = requests.request("GET",
                                      liveEvent.get("url"),
                                      headers=liveEvent.get("headers"),
                                      data=liveEvent.get("payload"))
# response = response = requests.get(url, headers=headers)
responseLiveEvents_dict = json.loads(responseLiveEvents.text)
# save live event
savefile('data/01_LiveEvents.json', responseLiveEvents_dict)

for event in responseLiveEvents_dict['data']:
    print(50*"#")
    print(f'{event}')
    if event["categoryId"] == "1":
        fixturePopularity = event['fixturePopularity']
        for eventId, val in fixturePopularity.items():
            eventConfig = eventMatch(eventId)
            print(eventConfig['url'])
            responseEvent = requests.get(
                eventConfig['url'],
                headers=eventConfig['headers'])
            responseEvent_dict = json.loads(responseEvent.text)
            # save event
            savefile(
                f'data/02_event_{eventId}_widgets.json',
                responseEvent_dict)
            # widgets
            widgets = responseEvent_dict['data']['widgets']
            for widget in widgets:
                
                print(widget['data']['data']['matchClock'])
                
                
                # savefile(
                #     f'data/02_event_{eventId}_selections.json',
                #     widget['data']['data']['selections']
                #     )
