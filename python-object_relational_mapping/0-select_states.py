#!/usr/bin/python3
"""
Module that get all states from a database.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # connexion
    connexion = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # cursor creation
    cursor = connexion.cursor()

    # SQL query execution
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # get the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connexion.close()
