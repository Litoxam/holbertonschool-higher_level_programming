#!/usr/bin/python3
"""
 Takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches the argument.
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
    cursor.execute("SELECT * FROM states where name = '{}' ORDER BY id ASC"
                   .format(sys.argv[4]))

    # get the result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connexion.close()
