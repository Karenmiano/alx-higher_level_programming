#!/usr/bin/python3
"""lists state id of object with the name passed as argument."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).filter(State.name == (argv[4],)) \
                                 .order_by(State.id)
    if record:
        print(record[0].id)
    else:
        print("Not Found")
