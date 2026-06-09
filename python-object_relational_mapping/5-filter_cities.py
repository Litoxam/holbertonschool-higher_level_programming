#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC ", (sys.argv[4],))

    # get the result
    rows = cursor.fetchall()

    first_city = True
    for row in rows:
        if not first_city:  # starting from the second city name
            print(", ", end="")  # space before the name of the city
        print(row[0], end="")
        first_city = False
    print()
    cursor.close()
    connexion.close()
