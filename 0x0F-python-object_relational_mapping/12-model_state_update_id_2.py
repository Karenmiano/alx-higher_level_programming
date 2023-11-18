#!/usr/bin/python3
"""changes the name attribute of object id=2 to New Mexico."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    get_state = session.query(State).filter(State.id == 2).first()
    get_state.name = 'New Mexico'
    session.commit()
