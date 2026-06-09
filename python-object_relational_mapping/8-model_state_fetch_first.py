#!/usr/bin/python3
"""
List all State objects from the database.
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(user, password, database)
    )

Session = sessionmaker(bind=engine)
session = Session()

# Reminder : the 'states' table is mapped to the State class.
# Retrieve all State objects ordered by id.
states = session.query(State).first()

# Print each state with its id and name.
if State is None:
    print("Nothing")
else:
    print("{}: {}".format(states.id, states.name))


# Close the session when finished.
session.close()
