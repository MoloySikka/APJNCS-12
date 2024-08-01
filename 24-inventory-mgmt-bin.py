import mysql.connector as sql_con

con = sql_con.connect(
    host="localhost",
    username="root",
    passwd="mysql@123",
    database="stationery"
)

cur = con.cursor()


def AddItem():
    ino = input("Ino: ")
    i_name = input("Name: ")
    qty = input("Qty: ")
    price = input("Price: ")
    dot = input("Date(YYYY-MM-DD): ")
    trans = "S"
    sql = "INSERT INTO ISTOCK VALUES ({},'{}',{},{},'{}','{}')".format(ino, i_name, qty, price, dot, trans)
    cur.execute(sql)
    con.commit()
    sql = "SELECT count(*) FROM ISTOCK"
    cur.execute(sql)
    r = cur.fetchall()
    print(r, "Items in stock ")


def ViewItems():
    sql = "SELECT * FROM ISTOCK"
    cur.execute(sql)
    r = cur.fetchall()
    for ino, name, price, qty, dot, tr in r:
        print("%4d|%20s|%5d|%8.2f|%12s|%2s" % (ino, name.ljust(20, " "), price, qty, dot, tr))


def SearchItem():
    ino = input('Ino: ')
    sql = "SELECT * FROM ISTOCK WHERE Ino = {} ".format(ino)
    cur.execute(sql)
    r = cur.fetchone()
    if int(r[0]) == int(ino):
        print('Found .......')
        print('Ino :', r[0])
        print('Item :', r[1])
        print('Price :', r[2])
        print('Quantity :', r[3])
        print('Last transaction done on :', r[4])
        Stats = "Purchase" if r[5] == "P" else "Sale"
        print('Last transaction :', Stats)


def BuyItem():
    ino = input('Ino: ')
    sql = "SELECT count(*) FROM ISTOCK WHERE INO = {}".format(ino)
    cur.execute(sql)
    r = cur.fetchone()[0]
    if r > 0:
        qty = input("Qty bought: ")
        dot = input("Date[YYYY-MM-DD]: ")
        trans = "P"
        sql = "UPDATE ISTOCK SET Qty=Qty+{} , DOT='{}', TRANS='{}' WHERE Ino={}".format(qty, dot, trans, ino)
        cur.execute(sql)
        con.commit()


def IssueItem():
    ino = input("Ino: ")
    sql = "SELECT * FROM ISTOCK WHERE Ino={}".format(ino)
    cur.execute(sql)
    r = cur.fetchone()[0]
    if r > 0:
        qty = input('Quantity to be issued: ')
        sql = "SELECT Qty FROM ISTOCK WHERE Ino = {}".format(ino)
        cur.execute(sql)
        r_qty = cur.fetchone()[0]
        if r_qty >= int(qty):
            dot = input("Date[YYYY-MM-DD]: ")
            trans = "I"
            sql = "UPDATE ISTOCK SET Qty=Qty-{}, DOT = '{}', Trans= '{}' WHERE Ino={}".format(qty, dot, trans, ino)
            cur.execute(sql)
            con.commit()
            sql = "SELECT Qty FROM ISTOCK WHERE Ino = {}".format(ino)
            cur.execute(sql)
            r = cur.fetchone()[0]
            print("Quantity updated in stock: {}, for Ino: {}".format(r, ino))
        else:
            print("Quantity is not sufficient in stock.")
    else:
        print("Ino: {} not found in stock".format(ino))


print("--------------STORE MANAGEMENT SYSTEM--------------")
while True:
    print("\nA : Add item \nV : View item \nS : Search item \nB : Buy item \nI : Issue item \nQ : Quit")
    user_input = input("\nType the respective letter for the appropriate command: ")
    if user_input == "A":
        AddItem()
    elif user_input == "V":
        ViewItems()
    elif user_input == "S":
        SearchItem()
    elif user_input == "B":
        BuyItem()
    elif user_input == "I":
        IssueItem()
    elif user_input == "Q":
        con.close()
        break
    else:
        print('Wrong input.')
