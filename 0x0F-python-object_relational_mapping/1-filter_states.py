#!/usr/bin/python3
""" list states Starting with N.
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
        c.execute("""SELECT * FROM states WHERE states.name LIKE BINARY 'N%'
                  ORDER BY states.id""")
        for i in c.fetchall():
            print(i)
        c.close()
        db.close()
