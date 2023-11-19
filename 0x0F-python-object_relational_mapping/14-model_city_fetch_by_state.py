#!/usr/bin/python3
"""prints all cities and their states from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State.name, City.id, City.name) \
                     .join(State).order_by(City.id)
    for state, city_id, city in records:
        print("{}: ({}) {}".format(state, city_id, city))
