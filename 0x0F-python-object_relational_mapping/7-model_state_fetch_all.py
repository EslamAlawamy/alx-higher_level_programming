#!/usr/bin/python3
""" 7. All states via SQLAlchemy """
from sys import argv
from SQLAlchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """ lists all State objects from the database hbtn_0e_6_usa """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:5432/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
