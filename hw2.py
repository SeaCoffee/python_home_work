'''

from functools import wraps

from typing import Callable, List, Tuple


1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи


def notebook():
    todo_list = []

    def add_todo(todo):
        todo_list.append(todo)

    def get_all():
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()


add_todo('do homework')
add_todo('check homework')
print(get_all())


2) протипізувати перше завдання


def notebook() -> Tuple[Callable[[str], None], Callable[[], List[str]]]:
    todo_list: List[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> List[str]:
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo('do homework')
add_todo('check homework')
print(get_all())


3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'


def expanded_form(num: int) -> str:
    num_str = str(num)
    length = len(num_str)
    result = []

    for i in range(length):
        if num_str[i] != '0':
            result.append(num_str[i] + '0' * (length - i - 1))

    return ' + '.join(result)

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'

4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
та буде виводити це значення після виконання функцій





def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'count {wrapper.count}')
        return result
    wrapper.count = 0
    return wrapper

@countcall
def func1():
    print('func1')

@countcall
def func2():
    print('func2')


func1()
func2()
func1()
func1()
func2()
func1()
func2()
"""



