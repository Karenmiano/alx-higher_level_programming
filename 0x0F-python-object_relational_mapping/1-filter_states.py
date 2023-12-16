#!/usr/bin/python3
"""lists all states from database starting with N"""

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
    cur.execute("""SELECT * from states WHERE BINARY name LIKE 'N%'
                ORDER BY id ASC""")
    results = cur.fetchall()        
    for record in results:
        print(record)
    cur.close()
    db.close()
