#!/usr/bin/python3
"""states"""


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
    curs.execute('SELECT * FROM `states` WHERE `name` LIKE BINARY "N%%";')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
