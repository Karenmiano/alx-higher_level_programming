#!/usr/bin/python3

from sqlalchemy import create_engine
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker

engine = create_engine("""mysql://{}:{}@localhost:3306/{}""".format(argv[1],
                          argv[2], argv[3]))
Session = sessionmaker(bind = engine)
session = Session()
records = session.query(State).all()
for record in records:
    print("{}: {}".format(record.id, record.name))
