#!/usr/bin/python3
""" 2. Filter states by user input """
from sys import argv
import MySQLdb


if __name__ == '__main__':
    """
    script that takes in an argument
    and displays all values in the states
    where name matches the argument
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE '{}' \
                ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
