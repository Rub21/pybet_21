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
        if market["marketFriendlyName"] == "Match winner":
            print(market["lineValueRaw"], market["id"], market["status"], market["deadline"])


def get_event_selections(selections):
    listOptions = ["HOME", "DRAW", "AWAY"]
    marketInfo = {}
    for selection in selections:
        selectionTemplateId = selection["selectionTemplateId"]
        if selectionTemplateId in listOptions:
            marketInfo[selectionTemplateId] = {
                # 'selectionTemplateId':selectionTemplateId,
                "odds": selection["odds"],
                "status": selection["status"],
                "label": selection["label"],
                "id": selection["id"],
            }
    return marketInfo


def filterMainMarkets(selectionsObj):
    new_selectionsObj = []
    for selection in selectionsObj:
        if "-MW3W-" in selection["id"] or "-MW2W-" in selection["id"]:
            new_selectionsObj.append(selection)
    return new_selectionsObj


def analyse_markets(eventInfo, markets, slug):
    # listOptions = ['HOME', 'DRAW', 'AWAY']
    eventId = eventInfo["eventId"]
    minutes = eventInfo["minutes"]
    seconds = eventInfo["seconds"]

    slug_list = slug.split("/")
    message = f'{20*"#"} {minutes}:{seconds}\n'

    message += f"https://www.betsson.com/pe/apuestas-deportivas/futbol/*/{slug_list[2]}/{slug_list[3]}?eventId={eventId}&eti=0&fs=true\n"
    # https://www.betsson.com/pe/apuestas-deportivas/futbol/otras-ligas-sudamerica/colombia-primera-a/millonarios-atletico-bucaramanga?eventId=f-vsbHNussQEennEBlz53yEQ&eti=1
    print(f"{message}")

    bet = False
    for market in markets:
        odds = market["odds"]
        selectionTemplateId = market["selectionTemplateId"]
        label = market["label"]

        # and selectionTemplateId in listOptions
        odds_eval = odds > 1.0 and odds <= 2
        odds_eval = True
        tiempo = ""
        if minutes >= 35 and minutes <= 47 and odds_eval:
            bet = True
            tiempo = "primer_tiempo"
            message += f"{label}--{odds}\n"

        if minutes >= 80 and odds_eval:
            bet = True
            tiempo = "segundo_tiempo"
            message += f"{label}----{odds}\n"

    return {"message": message, "bet": bet, "tiempo": tiempo}
