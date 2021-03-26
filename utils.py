def get_event_details(event):
    participants = event["participants"]
    obj = {"eventId": event["eventId"], **event["matchClock"]}
    for index, participant in enumerate(participants):
        id = participant["id"]
        index = index + 1
        obj[f"t{index}_id"] = id
        obj[f"t{index}_team"] = participant["label"]
        obj[f"t{index}_score"] = event["scorePerParticipant"][id]
    return obj

def get_event_markets(markets):
    for market in markets:
        if market['marketFriendlyName'] == "Match winner":
            print(market['lineValueRaw'], market['id'],
                  market['status'], market['deadline'])

def get_event_selections(selections):
    listOptions = ['HOME','DRAW','AWAY']
    marketInfo = {}
    for selection in selections:
        selectionTemplateId = selection["selectionTemplateId"]
        if selectionTemplateId in  listOptions:
            marketInfo[selectionTemplateId] = {
                # 'selectionTemplateId':selectionTemplateId,
                'odds':selection['odds'],
                'status':selection['status'],
                'label':selection['label'],
                'id':selection['id']
            }
    return marketInfo


def analyse_event(events, evaluteMinute):
    message=''

    print('########################events')
    print(f'{events}')
    print('########################')
    
    for event in events:
        # print(event['seconds'],event['seconds'])
        eventId= event['eventId']
        minutes= event['minutes']
        seconds= event['seconds']
        t1_id = event["t1_id"]
        t1_team = event["t1_team"]
        t1_score = event["t1_score"]
        t2_id = event["t2_id"]
        t2_team = event["t2_team"]
        t2_score = event["t2_score"]

        if minutes > evaluteMinute:
            message += f'{20*"#"} {minutes}:{seconds}\n'
            message  +=  f'https://www.betsson.com/pe/apuestas-deportivas/en-vivo/futbol?eventId={eventId}&eti=0\n'
            if event.get('HOME', "*") != "*":
                odds = event.get('HOME')["odds"]
                status = event.get('HOME')["status"]
                message += f'HOME: {t1_team}({t1_score})-->{odds}({status})\n'

            if event.get('AWAY', "*") != "*":
                odds = event.get('AWAY')["odds"]
                status = event.get('AWAY')["status"]
                message += f'AWAY: {t2_team}({t2_score})-->{odds}({status})\n'

            if event.get('DRAW', "*") != "*":
                odds = event.get('DRAW')["odds"]
                status = event.get('DRAW')["status"]
                message += f'DRAW > {odds}[{status}]'
            # message += '\n\n\n\n'
    return message