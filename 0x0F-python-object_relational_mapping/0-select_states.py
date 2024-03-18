#!/usr/bin/python3
'''lists all states from database hbtn_0e_0_usa'''


import MySQLdb
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db = argv[3]
    database = MySQLdb.connect(port=3306,
                               host='localhost',
                               charset='utf8',
                               user=user,
                               passwd=password,
                               db=db)
    curs = database.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
