#!/usr/bin/python3
"""
 a script that deletes all State objects
 with a name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    cities = (session.query(City, State)
                     .join(State, City.state_id == State.id)  # joins tables
                     .order_by(City.id)  # orders by City.id
                     .all()
              )

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session.
    session.close()
