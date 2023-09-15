#!/usr/bin/python3
""" 12. Update a state """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ adds the State object “Louisiana” to the database hbtn_0e_6_usa """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    stateUpdated = session.query(State).filter(State.id == 2).first()
    stateUpdated.name = "New Mexico"
    session.commit()
