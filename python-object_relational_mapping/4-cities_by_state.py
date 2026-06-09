#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # connexion
    connexion = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
    )
    # cursor creation
    cursor = connexion.cursor()

    # SQL query execution
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states "
                   "INNER JOIN cities "
                   "ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC;")

    # get the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connexion.close()
