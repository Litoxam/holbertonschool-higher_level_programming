#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(user, password, database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # The 'states' table is mapped to the State class.
    # Retrieve all states containing the letter 'a', ordered by id.
    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)\
                    .all()

    # Display each state's id and name.
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session.
    session.close()
