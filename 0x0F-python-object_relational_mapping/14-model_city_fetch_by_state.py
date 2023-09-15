#!/usr/bin/python3
""" 14. Cities in state """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ = "__main__":
    """ prints all City objects from the database hbtn_0e_14_usa """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    st_cty = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
