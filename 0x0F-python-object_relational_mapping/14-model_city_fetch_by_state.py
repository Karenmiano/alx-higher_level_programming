#!/usr/bin/python3
"""lists all cities with states from hbtn_0e_14_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name).join(
              State).order_by(City.id).all()
    for record in results:
        print(f'{record[0]}: ({record[1]}) {record[2]}')
