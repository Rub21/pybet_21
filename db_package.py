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


def get_Events():
    events = session.query(Market.event_id).group_by(Market.event_id).all()
    for event in events:
        eventId = event[0]
        markets = session.query(Market).filter(Market.event_id == eventId)
        markets_dict = {}
        for market in markets:
            id_ = market.id_

            evt = {
                "odds": market.odds,
                "minutes": market.minutes,
            }

            if id_ in markets_dict.keys():
                markets_dict[id_]["data"].append(evt)
            else:
                markets_dict[id_] = {"label": market.label, "data": [evt]}


# get_Events()
