#!/usr/bin/env python3
""" SQL injection safe state name entry
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db_name = sys.argv[3]
        db = MySQLdb.connect(host="localhost", port=3307, user=user,
                             password=pwd, database=db_name)
        c = db.cursor()
        c.execute("""SELECT cities.id, cities.name, states.name
                  FROM states, cities where cities.state_id = states.id
                  ORDER BY cities.id""")
        for i in c.fetchall():
            print(i)
        c.close()
        db.close()
