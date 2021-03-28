from db_classes import Event, Market, Base
from db_connection import _get_session
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

        # print('########################')
        # print(f'{mrkInfo}')
        # print('########################')
        
        session.add(Market(
            # time
            event_id=eventInfo['eventId'],
            seconds=eventInfo['seconds'],
            minutes=eventInfo['minutes'],

            # Teams
            t1_id=eventInfo['t1_id'],
            t1_team=eventInfo['t1_team'],
            t1_score=eventInfo['t1_score'],
            t2_id=eventInfo['t2_id'],
            t2_team=eventInfo['t2_team'],
            t2_score=eventInfo['t2_score'],

            # markets
            market_id=mrkInfo['marketId'],
            odds=mrkInfo['odds'],
            alternate_label=mrkInfo['alternateLabel'],
            status=mrkInfo['status'],
            sort_order=mrkInfo['sortOrder'],
            participant_label=mrkInfo['participantLabel'],
            selection_template_id=mrkInfo['selectionTemplateId'],
            id_=mrkInfo['id'],
            label=mrkInfo['label']
        ))

    session.commit()


def get_Events():
    query = session.query(Market).group_by(Market.eventId).all()

    # session.query(Table.column, func.count(Table.column)).group_by(Table.column).all()

    for q in query:
        print(q)

def get_Markets(eventId):
    query = session.query(Market)
    # . \filter(Building.neighborhood == neighborhood)
    for q in query:
        print(q)

# get_Events()