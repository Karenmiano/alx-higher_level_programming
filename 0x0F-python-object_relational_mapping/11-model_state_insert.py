#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("""mysql://{}:{}@localhost:
                              3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()
    state_id = session.query(State).filter(State.name == "Louisiana").first()
    print(state_id.id)
