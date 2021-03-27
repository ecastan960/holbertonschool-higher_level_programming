#!/usr/bin/python3
"""script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """This code its not executed if imported
    """

    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()

    for eachRow in rows:
        if eachRow[1][0] == 'N':
            print(eachRow)
    c.close()
    conn.close()
