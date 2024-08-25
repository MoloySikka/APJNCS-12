# 21/8/24
# AIM: To demonstrate the basic operations of a stack, implemented using a Python list.

mystack = []


def fillStack():
    for i in range(5):
        a = int(input('Enter number: '))
        mystack.append(a)


fillStack()


def push():
    a = int(input('Enter number to be pushed: '))
    mystack.append(a)
    print('\nUpdated stack is: ', mystack)


def pop():
    mystack.pop()
    print('\nUpdated stack is: ', mystack)


def peek():
    print(mystack[-1])


while True:
    text = "\nWould you like to: \npush (1) \npop  (2) \npeek (3) \nexit (4): "
    ans = int(input(text))
    if ans == 1:
        push()
    elif ans == 2:
        pop()
    elif ans == 3:
        peek()
    elif ans == 4:
        print('Thank you for using the program')
        break
    else:
        print('Please enter respective number.')
