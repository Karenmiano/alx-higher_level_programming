#!/usr/bin/python3
"""Delete states with a in hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like("%a%")).delete(
            synchronize_session='fetch')
    session.commit()
