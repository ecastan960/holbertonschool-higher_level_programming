#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument with safeguard
against MySQL injections
"""
import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
d_name = argv[3]
state_name = argv[4]

if __name__ == '__main__':
    """This code its not executed if imported
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    c = conn.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON \
             cities.state_id=states.id WHERE states.name = %(state_name)s "
    c.execute(query, {'state_name': state_name})
    rows = c.fetchall()
    count = 0

    for eachRow in rows:
        if len(rows) - 1 > count:
            print('{}, '.format(eachRow[0]), end="")
        else:
            print('{}'.format(eachRow[0]))
        count += 1