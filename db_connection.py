from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound


from db_classes import Event, Base


def _get_session(db_url, use_batch_mode=True, echo=False):
    """Helper to get an SQLAlchemy DB session"""
    # `use_batch_mode` is experimental currently, but needed for `executemany`
    engine = create_engine(db_url, echo=echo)  # use_batch_mode=use_batch_mode,
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        connection = session.connection()
        print("Successfully connected to database.")
    except:
        raise RuntimeError(f"Couldn't connect to db: {db_url}")
    return session
