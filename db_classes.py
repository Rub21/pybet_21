"""
Database objects for storing Housing Passports-relevant data

@author: Development Seed
"""
from collections import Counter

from sqlalchemy import (Column, Integer, String, Float,
                        ForeignKey)
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Set the declarative base to prep creation of SQL classes
Base = declarative_base()


class Event(Base):

    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    eventId = Column(String)
    seconds = Column(Integer)
    minutes = Column(Integer)
    gameClockMode = Column(String)
    lastDateTimeSet = Column(String)

    t1_id = Column(Integer)
    t1_team = Column(String)
    t1_score = Column(Integer)
    t2_id = Column(Integer)
    t2_team = Column(String)
    t2_score = Column(Integer)
    markets = Column(JSONB)

    def __repr__(self):
        """Define string representation."""
        return f'<Building(n_detections={len(self.detections)}, neighborhood={self.neighborhood})>'


class Market(Base):

    __tablename__ = 'market'
    id = Column(Integer, primary_key=True)

    event_id = Column(String)
    seconds = Column(Integer)
    minutes = Column(Integer)

    t1_id = Column(Integer)
    t1_team = Column(String)
    t1_score = Column(Integer)
    t2_id = Column(Integer)
    t2_team = Column(String)
    t2_score = Column(Integer)

    market_id = Column(String)  # "m-f-_CRDlF5TjkyyaGWgKAnHEg-MTG2W-4.5",
    odds = Column(Float)  # 51.0,
    alternate_label = Column(String)  # "Over 4.5",
    status = Column(String)  # "Open",
    sort_order = Column(Integer)  # 1,
    participant_label = Column(String)  # "Over 4.5",
    selection_template_id = Column(String)  # "OVER",
    id_ = Column(String)  # "s-m-f-_CRDlF5TjkyyaGWgKAnHEg-MTG2W-4.5-over",
    label = Column(String)  # "Over 4.5"

