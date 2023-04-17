#!/usr/bin/python3
""" Use stateName as input and use it to select states.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pwd = sys.argv[2]
        db_name = sys.argv[3]
        stateName = sys.argv[4]
        db = MySQLdb.connect(host="localhost", port=3307, user=user,
                             password=pwd, database=db_name)
        c = db.cursor()
        c.execute("""SELECT * FROM states WHERE BINARY states.name = '{}'
                  ORDER BY states.id""".format(stateName))
        states = c.fetchall()
        for i in states:
            print(i)
        c.close()
        db.close()
