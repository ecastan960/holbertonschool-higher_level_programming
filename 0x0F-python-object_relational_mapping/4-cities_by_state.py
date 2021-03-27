#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
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
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id=states.id \
             ORDER BY cities.id ASC"
    c.execute(query)
    rows = c.fetchall()

    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
