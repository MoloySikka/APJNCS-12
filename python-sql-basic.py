# not quite sure bout this one

import mysql.connector

db1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sql@321',
    database='db1'
)

cursor = db1.cursor()

cursor.execute('select * from stud;')
r = cursor.fetchall()

for i in r:
    print(f'R.no: {i[0]} | Name: {i[1].ljust(20, '_')} | Date of Birth: {i[2].day}/{i[2].month}/{i[2].year} | Phone no: {i[3]}')
