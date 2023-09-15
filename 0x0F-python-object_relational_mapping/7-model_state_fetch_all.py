#!/usr/bin/python3
""" 7. All states via SQLAlchemy """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ lists all State objects from the database hbtn_0e_6_usa """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(states.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
