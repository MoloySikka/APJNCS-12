import pickle

data = [
    ['football', 'Kangaroos', 11],
    ['football', 'Wombats', 11],
    ['basketball', 'Risers', 10],
    ['basketball', 'Fells', 10],
    ['cricket', 'India', 11]
]

for i in data:
    try:
        with open('sports.dat', 'ab') as sports:
            pickle.dump(i, sports)

    except FileNotFoundError:
        with open('sports.dat', 'ab') as sports:
            pickle.dump(i, sports)


def copy_data():
    basket_dat = []
    with open('sports.dat', 'rb') as _sports:
        while True:
            try:
                r = pickle.load(_sports)
                print(r)
                if r[0] == 'basketball':
                    basket_dat.append(r)

            except EOFError:
                break

    with open('basket.dat', 'wb') as basket:
        pickle.dump(basket_dat, basket)

    print(f'No. of records: {len(basket_dat)}')

copy_data()

