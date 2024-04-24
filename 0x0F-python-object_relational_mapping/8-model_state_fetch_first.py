#!/usr/bin/python3
'''script that prints the first State object'''


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print('Nothing')

    session.close()
