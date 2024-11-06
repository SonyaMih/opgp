import random

width = 3
height = 5

list = []

for i in range(height):
    list2 = []
    for j in range(width):
        number = random.randint(-9999,99999)
        list2.append(number)
    list.append(list2)

for riadok in list:
    for objekt in riadok:
        print(f'|{objekt:5}', end='')
    print('|')