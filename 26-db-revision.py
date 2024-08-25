# 10/07/2024
# AIM: WAP To create a database named 'company' with a table named 'project', add three records, and increase the number of people by 2 in all projects.

import mysql.connector as db

con = db.connect(
    host='localhost',
    user='root',
    password='mysql@123',
)
cur = con.cursor()

SQL_query = "CREATE DATABASE COMPANY;"
cur.execute(SQL_query)
SQL_query = "USE COMPANY;"
cur.execute(SQL_query)

SQL_query = "CREATE TABLE PROJECT(PROJECT_NO INT, TITLE CHAR(30), NO_OF_PEOPLE INT(2), STATUS CHAR(20));"
cur.execute(SQL_query)
SQL_query = ("INSERT INTO PROJECT VALUES(1,'PROJECT 1', 2,'ONGOING'), (2,'PROJECT 2', 3,'ONGOING'), (3,'PROJECT 3', 3,"
             "'COMPLETED');")
cur.execute(SQL_query)
con.commit()

cur.execute('SELECT * FROM PROJECT;')
r = cur.fetchall()

for no, title, num_per, stats in r:
    print(str(no).ljust(2) + title.center(20) + str(num_per).ljust(2) + stats.center(20))

cur.execute("UPDATE PROJECT SET NO_OF_PEOPLE = NO_OF_PEOPLE + 2;")
con.commit()

print('\nUpdated table is:\n')
cur.execute('SELECT * FROM PROJECT;')
r = cur.fetchall()

for no, title, num_per, stats in r:
    print(str(no).ljust(2) + title.center(20) + str(num_per).ljust(2) + stats.center(20))

con.close()
