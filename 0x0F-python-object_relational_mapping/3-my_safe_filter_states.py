#!/usr/bin/python3
"""lists state from database where name is Arizona"""

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
    match = argv[4]
    cur.execute("""SELECT * FROM states WHERE BINARY name LIKE %s
                ORDER BY id ASC""", (match, ))
    results = cur.fetchall()
    for record in results:
        print(record)
    cur.close()
    db.close()
