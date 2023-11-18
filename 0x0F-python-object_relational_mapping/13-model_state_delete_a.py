#!/usr/bin/python3
"""deletes records with names having letter a in them."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).filter(State.name.like('%a%')).all()
    for record in records:
        session.delete(record)
    session.commit()
