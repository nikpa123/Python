phone_book = []
path = 'file.txt'

def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)

def save_file(phone_book, path):
    save_list = []
    for i in range(len(phone_book)):
        save_list.append(';'.join(phone_book[i]))
    data = '\n'.join(save_list)
    file = open(path, 'w', encoding='UTF-8')
    file.write(data)
    file.close()

def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')

def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))

def search_contact(phone_book):
    search = input('Поиск:' )
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)

def change_contact(phone_book):
    show_contacts(phone_book)
    n = int(input("Введите номер контакта, который вы хотите изменить: "))
    while True:
        print('''    1. Изменить имя и фамилию
    2. Изменить номер телефона
    3. Изменить комментарий
    4. Выход''')
        number = int(input('Введите пункт меню: '))
        match number:
            case 1:
                phone_book[n - 1][0] = input('Введите имя и фамилию: ')
                print(phone_book[n - 1])
            case 2:
                phone_book[n - 1][1] = input('Введите телефон: ')
                print(phone_book[n - 1])
            case 3:
                phone_book[n - 1][2] = input('Введите комментарий: ')
                print(phone_book[n - 1])
            case 4:
                break

def delete_contact(phone_book):
    show_contacts(phone_book)
    n = int(input("Введите номер контакта, который вы хотите удалить: "))
    phone_book.pop(n - 1)


while True:
    print('''Главное меню: 
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    number = int(input('Введите пункт меню: '))
    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            save_file(phone_book, path)
            print('Файл сохранён')
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            change_contact(phone_book)
        case 6:
            search_contact(phone_book)
        case 7:
            delete_contact(phone_book)
        case 8:
            break