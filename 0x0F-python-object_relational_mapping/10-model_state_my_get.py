#!/usr/bin/python3
"""lists state id of object with the name passed as argument."""

from sqlalchemy import create_engine, text
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).filter(text("name=:name")) \
                                 .params(name=argv[4]) \
                                 .order_by(State.id)
    try:
        print(record[0].id)
    except IndexError:
        print("Not Found")
