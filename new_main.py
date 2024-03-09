# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1 Создать файл                                    +
#     1.1 Открыть файл на дозапись                  +
# 2 Запись контакта в файл
#     2.1 Открыть файл на дозапись
#     2.2 Получить данные из нового контакта
#     2.3 Записать эти данные в файл
# 3 Вывод данных на экран
#     3.1 Открыть файл на чтение 
#     3.2 Открыть данные из файла
#     3.3 Вывести данные на экран
# 4 Поиск контакта по данным
#     4.1 Получить данные для поиска
#     4.2 Выбрать вариант поиска
#     4.3 Открыть файл на чтение
#     4.4 Получить данные из файла
#     4.5 Осуществить поиск
#     4.6 Вывести на экран
# 5 Создать UI                                      ++++
#     5.1 Вывод на экран меню                       +
#     5.2 Получить запрос от пользователя           +
#     5.3 Запуск выбранной функции                  +
#     5.4 Выход из программы                        +


def input_name():
    return input('Введите имя: ')


def input_sername():
    return input('Введите фамилию: ')


def input_patronumic():
    return input('Введите отчество: ')


def input_phone():
    return input('Введите телефон: ')


def input_address():
    return input('Введите адрес: ')


def creat_contact():
    name = input_name()
    surname = input_sername()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f'{name} {surname} {patronumic} {phone}\n{address}\n\n'


def add_contact():
    contact = creat_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as f_w:
        f_w.write(contact)


def print_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split('\n\n')
    for i, contact in enumerate(list_contacts, 1):
        print(i, contact + '\n')


def find_contact():
    search = input('Введите данные для поиска: ')
    print(
        'Возможные варианты поиска:\n'
        '1. По имени\n'
        '2. По фамилии\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n'
    )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4'):
        print('Некорректный ввод данных')
        var = input('Выберите вариант поиск: ')
    i_var = int(var) - 1
    with open('phonebook.txt', 'r', encoding='utf-8') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split('\n\n')
    for contact in list_contacts:
        contact_lst = contact.split()
        print(contact_lst)
        if search in contact_lst[i_var]:
            print(contact)

def copy_line():
    pass


# UI
def ui():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    choise = '0'
    while choise != '4':
        print(
            'Возможные варианты действий: \n'
            '1. Добавление нового контакта\n'
            '2. Вывод данных на экран\n'
            '3. Поиск контакта\n'
            '4. Копировать строку в другой файл\n'
            '5. Выход из программы\n'
        )
        choise = input('Выберите вариант действия: ')

        while choise not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            choise = input('Выберите вариант действия: ')

        if choise == '1':
            add_contact()
        elif choise == '2':
            print_phonebook()
        elif choise == '3':
            find_contact()
        elif choise == '4':
            copy_line()
        else:
            print('Всего доброго!')


ui()



















