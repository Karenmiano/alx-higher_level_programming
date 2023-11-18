#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).first()
    if record is None:
        print("Nothing")
    else:
        print("{}: {}".format(record.id, record.name))