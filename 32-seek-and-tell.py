# 23/08/24
# AIM: Write a Python program to demonstrate the functionality of the seek() and tell() functions.

text = ['0123456789\n', 'abcdefghij\n', '0123456789\n', 'ABCDEFGHIJ\n', '0123456789\n']
with open('diary.txt', 'w') as diary:
    diary.writelines(text)

with open('diary.txt') as diary:
    diary.seek(5)
    print(f'\nPosition: {diary.tell()}')
    print(diary.read(5))
    diary.seek(10)
    print(f'\nPosition: {diary.tell()}')
    print(diary.read(5))
    diary.seek(15)
    print(f'\nPosition: {diary.tell()}')
    print(diary.read(5))
