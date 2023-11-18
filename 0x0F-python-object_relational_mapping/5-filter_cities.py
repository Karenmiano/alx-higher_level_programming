#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s""", (argv[4],))
    results = cur.fetchall()
    for record in results:
        city, = record
        print(city, end=", " if record != results[-1] else "\n")
    cur.close()
    db.close()
