#!/usr/bin/python3
"""lists cities from database and their linked states"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                JOIN states
                ON states.id = cities.state_id
                ORDER BY id ASC""")
    results = cur.fetchall()
    for record in results:
        print(record)
    cur.close()
    db.close()
