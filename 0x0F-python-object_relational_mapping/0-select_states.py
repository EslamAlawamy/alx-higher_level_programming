#!/usr/bin/python3
""" 0. Get all states """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    """ lists all states from the database """

    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
