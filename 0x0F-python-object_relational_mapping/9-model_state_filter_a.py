#!/usr/bin/python3
""" 9. Contains `a` """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ State objects that contain the letter a from database hbtn_0e_6_usa """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')) \
                    .order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
