#!/usr/bin/python3
"""List states with their cities hbtn_0e_101_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(State)
    for state in all_states:
        print(f'{state.id}: {state.name}')
        cities = state.cities
        for city in cities:
            print(f'    {city.id}: {city.name}')
