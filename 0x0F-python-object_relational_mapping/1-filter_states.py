#!/usr/bin/python3
""" 1. Filter states """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    """ lists all states with a name starting with N """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
