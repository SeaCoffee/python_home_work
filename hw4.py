import pickle

"""1) Є ось такий файл...
 ваша задача записати в новий файл тільки email'ли з доменом gmail.com
 (Хеш то що з ліва записувати не потрібно)



with open("emails.txt", "r") as file:
    with open("f2.txt", "a") as f:
        for row in file:
            columns = row.split()
            if columns[1].strip().endswith('gmail.com'):
                f.write(columns[1].strip() + '\n')




                2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)


def generate_id():
    try:
        with open("list.txt", "rb") as file:
            items = []
            while True:
                try:
                    items.append(pickle.load(file))
                except EOFError:
                    break
            if items:
                return max(item['id'] for item in items) + 1
            else:
                return 1
    except FileNotFoundError:
        return 1

def save_purchase():
    name = input("Назва: ")
    id = generate_id()
    price = float(input("Ціна: "))
    item = {'name': name, 'id': id, 'price': price}
    with open("list.txt", "ab") as file:
        pickle.dump(item, file)
    print("Добавлено")
def show_purchases():
    try:
        with open("list.txt", "rb") as file:
            while True:
                try:
                    item = pickle.load(file)
                    print(item)
                except EOFError:  
                    break
                except Exception as e: 
                    print("error: ", e)
                    break
    except FileNotFoundError:
        print("not found")


def max_price_purchase():
    max_price = 0
    max_price_item = None
    try:
        with open("list.txt", "rb") as file:
            while True:
                try:
                    item = pickle.load(file)
                    if item['price'] > max_price:
                        max_price = item['price']
                        max_price_item = item
                except EOFError:
                    break
                except Exception as e:
                    print("error: ", e)
                    break
        if max_price_item:
            print(max_price_item['name'], max_price_item['price'])
        else:
            print("not found")
    except FileNotFoundError:
        print("not found")

def find_purchase_by_id():
    search_id = int(input("Введіть id: "))
    found = False
    try:
        with open("list.txt", "rb") as file:
            while True:
                try:
                    item = pickle.load(file)
                    if item['id'] == search_id:
                        print(item)
                        found = True
                        break
                except EOFError:
                    break
                except Exception as e:
                    print("error: ", e)
                    break
        if not found:
            print("Покупки з таким id не знайдено")
    except FileNotFoundError:
        print("not found")
def main():
    while True:
        print("1. Добавити покупку")
        print("2. Список покупок")
        print("3. Найдорожча покупка")
        print("4. Знайти покупку по id")
        print("5. Вихід")
        cmd = input("Виберіть пункт: ")

        if cmd == "1":
            save_purchase()
        elif cmd == "2":
            show_purchases()
        elif cmd == "3":
            max_price_purchase()
        elif cmd == "4":
            find_purchase_by_id()
        elif cmd == "5":
            break
        else:
            print("Виберіть пунки з 1 по 4")

if __name__ == "__main__":
    main()



Є ось такий список:


потрібно брати по черзі с кожного списку id і класти в список res, 
якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122, .......]

"""
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

res_data = []


for sublist in data:
    for i in sublist:
        if i['id'] not in res_data:
            res_data.append(i['id'])

print(res_data)
