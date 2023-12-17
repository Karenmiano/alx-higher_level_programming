#!/usr/bin/python3
"""List cities with their states in hbtn_0e_101_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_cities = session.query(City).order_by(City.id)
    for city in all_cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
