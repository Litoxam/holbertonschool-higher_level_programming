#!/usr/bin/python3
"""
prog that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


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
    # Create a new State object.
    new_state = State(name="Louisiana")

    # Add the object to the session and commit the changes.
    session.add(new_state)
    session.commit()

    print(new_state.id)
    # Close the session.
    session.close()
