from db_classes import Event, Market, Base
from db_connection import _get_session
from graphs import create_line_graph

db_url = "postgresql://postgres:1234@db:5432/dbase"

session = _get_session(db_url)


def insert(eventInfo, marketInfo):
    # Store all messsages
    # session.add(Event(
    # eventId=eventInfo['eventId'],
    #                   seconds=eventInfo['seconds'],
    #                   minutes=eventInfo['minutes'],
    #                   gameClockMode=eventInfo['gameClockMode'],
    #                   lastDateTimeSet=eventInfo['lastDateTimeSet'],
    #                   t1_id=eventInfo['t1_id'],
    #                   t1_team=eventInfo['t1_team'],
    #                   t1_score=eventInfo['t1_score'],
    #                   t2_id=eventInfo['t2_id'],
    #                   t2_team=eventInfo['t2_team'],
    #                   t2_score=eventInfo['t2_score'],
    #                   markets=selectionsObj)
    #             )

    # marketInfo
    for mrkInfo in marketInfo:
        session.add(
            Market(
                # time
                event_id=eventInfo["eventId"],
                seconds=eventInfo["seconds"],
                minutes=eventInfo["minutes"],
                # Teams
                t1_id=eventInfo["t1_id"],
                t1_team=eventInfo["t1_team"],
                t1_score=eventInfo["t1_score"],
                t2_id=eventInfo["t2_id"],
                t2_team=eventInfo["t2_team"],
                t2_score=eventInfo["t2_score"],
                # markets
                market_id=mrkInfo["marketId"],
                odds=mrkInfo["odds"],
                alternate_label=mrkInfo["alternateLabel"],
                status=mrkInfo["status"],
                sort_order=mrkInfo["sortOrder"],
                participant_label=mrkInfo["participantLabel"],
                selection_template_id=mrkInfo["selectionTemplateId"],
                id_=mrkInfo["id"],
                label=mrkInfo["label"],
            )
        )

    session.commit()


def get_Events(limit):
    events = session.query(Market.event_id).group_by(Market.event_id).limit(limit)
    eventsList = {}
    for event in events:
        eventId = event[0]
        # eventsList[eventId]=[]

        # Check markets that has more that 50
        marketsSelected = session.execute(
            f"""
        SELECT count(event_id) as num_min , id_ from market where odds <= 2
        group by id_ ;
        
        """
        )
        #         where event_id='{eventId}' and
        # (	selection_template_id = 'HOME' or
        #     selection_template_id = 'AWAY' or
        #     selection_template_id = 'DRAW'
        # )
        # and odds < 1.5
        markets_evaluate = []
        for m in marketsSelected:
            # print()
            # if m[0] > 50:
            markets_evaluate.append(m[1])

        # get odds from markets
        markets = session.execute(
            f"SELECT event_id, minutes, seconds,  t1_score, t1_team,t2_team, t2_score, odds , id_, label from market  where event_id='{eventId}' order by minutes;"
        )
        markets_dict = {}
        for market in markets:
            id_ = market.id_

            title = f"{market.t1_team}({market.t1_score})----{market.t2_team}({market.t2_score})"
            if id_ in markets_evaluate:
                evt = {
                    "odds": market.odds,
                    "minutes": market.minutes,
                }
                if id_ in markets_dict.keys():
                    markets_dict[id_]["title"] = title
                    markets_dict[id_]["label"] = market.label
                    markets_dict[id_]["data"].append(evt)
                else:
                    markets_dict[id_] = {"data": [evt]}

        eventsList[eventId] = markets_dict
    return eventsList


def get_match_history(eventId, odds):
    markets = session.execute(
        f"SELECT event_id, minutes, seconds,  t1_score, t1_team,t2_team, t2_score, odds , id_, label from market  where event_id='{eventId}' and odds < {odds} order by minutes;"
    )
    markets_dict = {}
    for market in markets:
        id_ = market.id_
        title = f"{market.t1_team}({market.t1_score})----{market.t2_team}({market.t2_score})"
        evt = {
            "odds": market.odds,
            "minutes": market.minutes,
        }
        if id_ in markets_dict.keys():
            markets_dict[id_]["title"] = title
            markets_dict[id_]["label"] = market.label
            markets_dict[id_]["data"].append(evt)
        else:
            markets_dict[id_] = {"data": [evt]}
    return markets_dict
