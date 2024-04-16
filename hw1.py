'''
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:

st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.


st = 'as 23 fdfdg544'

st1 = ''

for i in st:
    if i.isdigit():
        st1 += i

st1_res = ','.join(st1)

print(st1_res)


2)написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі


st = 'as 23 fdfdg544 34'

result_str = ''.join(i if i.isdigit() else ' ' for i in st).split()

result_str = [int(num) for num in result_str]

print(result_str)

st = 'as 23 fdfdg544 34'

# OR

result_str = ''.join(i if i.isdigit() else ' ' for i in st).split()

result_str = [int(num) for num in result_str]

print(*result_str)



list comprehension

1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']


greeting = 'Hello, world'

res_greeting = [i for i in greeting.upper()]

print(res_greeting)

2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]


res = []

for i in range(0, 50):
    if i % 2 != 0:
        res.append(i**2)

print(res)


function

- створити функцію яка виводить ліст

list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]

def list_function(l):
    print(l)

list_function(list)


- створити функцію яка приймає три числа та виводить та повертає найбільше.


def comparison(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

comparison(25, 777, 666)


- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


def comparison2(*args):
        print(min(args))
        return(max(args))

comparison2(7,10,35,18,99,2005)



- створити функцію яка повертає найбільше число з ліста


def large(arr):
    max_num = arr[0]
    for i in arr:
        if i > max_num:
           max_num = i
    return max_num


list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
result = large(list)
print(result)


- створити функцію яка повертає найменьше число з ліста


def minimal(arr):
    min_num = arr[0]
    for i in arr:
        if i < min_num:
           min_num = i
    return min_num


list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
result = minimal(list)
print(result)

- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]

def add(arr):
    sum = 0
    for i in arr:
        sum +=i
    return sum

res = add(list)
print(res)

- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.



list1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]

def average(arr):
    sum = 0
    for v in arr:
        sum += v
    return sum/len(arr)

res = average(list1)
print(res)



# 1)Дан list:

list = [22, 3,5,2,8,2,-23, 8,23,5]

# - знайти мін число


res1 = print(min(list))


#  - видалити усі дублікати

print(set(list))

#  - замінити кожне 4-те значення на 'X'


for i in range(0,len(list),4):
    list[i] = 'X'

print(list)


#2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def stars_square(side_length):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            for j in range(20):
                print('*', end='')
        else:
            print('*', end='')
            for j in range(1, 19):
                print(' ', end='')
            print('*', end='')
        print()

stars_square(10)




# 3) вывести табличку множення за допомогою цикла while


number = 1

while number <= 10:
    count = 1
    while count <= 10:
        print(f"{number} x {count} = {number * count}")
        count += 1
    print()
    number += 1


#OR

i = 1
j = 1

while i <= 10:
    while j <= 10:
        print(f"{i*j:4}", end="")
        j += 1
    print()
    i += 1
    j = 1


# 4 переробити це завдання під меню

 '''


def menu():
    lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    while True:
        user_choice = input('Дано список: 22, 3, 5, 2, 8, 2, -23, 8, 23, 5\n'
                            'Завдання:\n'
                            '1.  - знайти мін число\n'
                            '2. видалити усі дублікати\n'
                            '3. замінити кожне 4-те значення на "X"\n'
                            '4. вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції\n'
                            '5. вывести табличку множення за допомогою цикла while\n'
                            'Ваш вибір: ')

        if user_choice == '1':
            print('Мінімальне число:', min(lst))
        elif user_choice == '2':
            print('Список без дублікатів:', list(set(lst)))
        elif user_choice == '3':
            for i in range(3, len(lst), 4):
                lst[i] = 'X'
            print('Список після заміни:', lst)
        elif user_choice == '4':
            side_length = 10
            for i in range(side_length):
                if i == 0 or i == side_length - 1:
                    print('*' * side_length)
                else:
                    print('*' + ' ' * (side_length - 2) + '*')
        elif user_choice == '5':
            i = 1
            while i <= 10:
                j = 1
                while j <= 10:
                    print(f"{i * j:4}", end="")
                    j += 1
                print()
                i += 1
        else:
            print("Виберіть пункти меню лише з 1 по 5")


menu()


















