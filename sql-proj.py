# 17/5/24
# incomplete

# TODO: Remove
class DB:
    def commit(self):
        return


class MyCur:
    def execute(self, command):
        return


# TODO: Remove


db = DB()
my_cur = MyCur()


def AddItem():
    i_no = input('Ino:')
    i_name = input('Name: ')
    qty = input('Quantity: ')
    price = input('Price: ')
    dot = input('Date [YYYY-MM-DD]: ')
    sql = f'insert into istock values({i_no}, {i_name}, {price}, {qty}, {dot})'
    my_cur.execute(sql)
    db.commit()
    sql = 'select count(*) from istock'
    my_cur.execute(sql)
