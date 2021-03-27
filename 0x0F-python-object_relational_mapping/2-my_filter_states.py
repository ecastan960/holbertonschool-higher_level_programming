#!/usr/bin/python3
"""script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """This code its not executed if imported
    """
    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    c = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    c.execute(query.format(state_name))
    rows = c.fetchall()

    for eachRow in rows:
        if eachRow[1] == state_name:
            print(eachRow)
    c.close()
    conn.close()
