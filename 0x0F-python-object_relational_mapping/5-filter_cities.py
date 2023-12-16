#!/usr/bin/python3
"""lists cities from database belonging to partcular state"""

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
    cur.execute("""SELECT cities.name FROM cities
                JOIN states
                ON states.id = cities.state_id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC""", (argv[4], ))
    results = cur.fetchall()
    cities = [record[0] for record in results]
    print(*cities, sep=" ,")
    cur.close()
    db.close()
