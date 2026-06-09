#!/usr/bin/python3
"""
List all State objects from the database.
"""

from sqlalchemy import create_engine
from model_state import Base, State
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine("mysql+mysqldb://%s:%s@localhost:3306/%s",(user, password, database))

Session = sessionmaker(bind=engine)
session = Session()

# Reminder : the 'states' table is mapped to the State class.
# Retrieve all State objects ordered by id.
states = session.query(State).order_by(State.id).all()

# Print each state with its id and name.
for state in states:
    print("{}: {}".format(state.id, state.name))

# Close the session when finished.
session.close()
