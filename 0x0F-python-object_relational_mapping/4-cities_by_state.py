#!/usr/bin/python3
''' script that lists all cities from database
hbtn_0e_4_usa'''


from sys import argv
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    curs = database.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name\
                  FROM cities INNER JOIN states ON states.id=cities.state_id\
                  ORDER BY cities.id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
