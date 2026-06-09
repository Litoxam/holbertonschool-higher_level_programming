#!/usr/bin/python3
"""
Display the first State object from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

# The 'states' table is mapped to the State class.
# Retrieve the first state.
state = session.query(State).first()

# Display the state's id and name.
if state is None:
    print("Nothing")
else:
    print("{}: {}".format(state.id, state.name))

# Close the session.
session.close()
