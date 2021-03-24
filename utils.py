def get_event_details(event):
    participants = event["participants"]
    obj = {"eventId": event["eventId"], **event["matchClock"]}
    for index, participant in enumerate(participants):
        id = participant["id"]
        index = index + 1
        obj[f"t{index}_id"] = id
        obj[f"t{index}_team"] = participant["label"]
        obj[f"t{index}_score"] = event["scorePerParticipant"][id]
    print(obj)


def get_event_markets(markets):
    for market in markets:
        if market['marketFriendlyName'] == "Match winner":
            print(market['lineValueRaw'], market['id'],
                  market['status'], market['deadline'])

def get_event_selections(selections):
    for selection in selections[0:3]:
        print(selection['participantLabel'],selection['odds'])