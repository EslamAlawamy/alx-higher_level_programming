#!/usr/bin/python3
""" 4. Cities by states """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    """ lists all cities from the database hbtn_0e_4_usa """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC;", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
