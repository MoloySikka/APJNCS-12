import mysql.connector

db1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql@123',
    database='students'
)

cursor = db1.cursor()
cursor.execute('select * from stud')
r = cursor.fetchall()

for i in r:
    print('R.no: ', i[0], ' | Name: ', i[1], ' | Date of Birth: ', i[2].day, '/', i[2].month, '/', i[2].year,
          ' | Phone no: ', i[3])

db1.close()
