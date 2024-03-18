#!/usr/bin/python3
"""states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db = argv[3]
    user_input = argv[4]
    database = MySQLdb.connect(user=user,
                               passwd=password,
                               db=db)
    curs = database.cursor()
    curs.execute('SELECT * FROM states WHERE name LIKE BINARY "{}"\
                  ORDER BY states.id ASC'.format(user_input))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
