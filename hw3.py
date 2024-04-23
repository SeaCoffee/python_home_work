from abc import ABC, abstractmethod

"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, sideX, sideY):
        self.sideX = sideX
        self.sideY = sideY

    def area(self):
        return self.sideX * self.sideY

    @staticmethod
    def sum(rectangle1, rectangle2):
        return rectangle1.area() + rectangle2.area()

    @staticmethod
    def dif(rectangle1, rectangle2):
        return rectangle1.area() - rectangle2.area()

    @staticmethod
    def isEqual(rectangle1, rectangle2):
        area1 = rectangle1.area()
        area2 = rectangle2.area()
        if area1 == area2:
            return 'equal'
        else: return 'not equal'

    @staticmethod
    def larger(rectangle1, rectangle2):
        area1 = rectangle1.area()
        area2 = rectangle2.area()
        if area1 < area2:
            return 'rectangle1 < rectangle2'
        else:
            return 'rectangle1 > rectangle2'

    def len(self):
        return self.sideX + self.sideY




rect1 = Rectangle(25, 10)
rect2 = Rectangle(666, 2)

res_sum_area = Rectangle.sum(rect1, rect2)

res_dif_area = Rectangle.dif(rect1, rect2)

res_is_equal = Rectangle.isEqual(rect1, rect2)

res_len_rect1 = rect1.len()

res_len_rect2 = rect2.len()


створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення




class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cindarella(Human):
    def __init__(self, name, age, footSize):
        super().__init__(name, age)
        self.footSize = footSize

class Prince(Human):
    def __init__(self, name, age, foundSize):
        super().__init__(name, age)
        self.foundSize = foundSize

    def looking(self, cindarellas_list):
        for i in cindarellas_list:
            if i.footSize == self.foundSize:
                print(i, 'The Same')
            else: print('looking forward')


cindarellas_list = [
    Cindarella('Ivanna', 18, 38),
    Cindarella('Ella', 28, 39),
    Cindarella('Alina', 20, 37),
    Cindarella('Sofia', 22, 36),

]


prince = Prince('Max', 23, 36)

prince.looking(cindarellas_list)

1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine
 инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

Приклад:

Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()

"""


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, newItem):
        if isinstance(newItem, (Book, Magazine)):
            cls.printable_list.append(newItem)

    @classmethod
    def show_all_magazines(cls):
        print("All Magazines:")
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        print("All Books:")
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
Main.show_all_books()
