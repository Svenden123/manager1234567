documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    '''
    спросит номер документа и выведет имя человека, которому он принадлежит
    '''
    number = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == number:
            print(doc['name'])
            return
    print('Документ не найден')


def people_all():
    '''
    выводит список всех владельцев документов
    '''
    names = []
    for doc in documents:
        try:
            names.append(doc['name'])
        except KeyError:
            print('У документа нет параметра "name"')
    print(*set(names), sep='\n')  # set используется для исключения повторов одно и того же имени


def list_docs():
    '''
    список всех документов в формате passport "2207 876234" "Василий Гупкин"
    '''
    for doc in documents:
        print('{} "{}" "{}"'.format(doc['type'], doc['number'], doc['name']))


def find_doc_in_directories(doc_number):
    for sh, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            return sh
    return None


def shelf():
    '''
    спросит номер документа и выведет номер полки, на которой он находится
    '''
    number = input('Введите номер документа: ')
    sh = find_doc_in_directories(number)
    if sh is None:
        print('Документ не найден')
    else:
        print(sh)


def add():
    '''
    добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки
    '''
    number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    name = input('Введите имя владельца: ')
    shelf = input('Введите номер полки ({}): '.format(
        ','.join(directories.keys())))
    if shelf not in directories:
        print('Неправильный номер полки')
        return
    documents.append({'type': doc_type, 'number': number, 'name': name})
    directories[shelf].append(number)
    print('Добавлено')


def delete():
    '''
    спросит номер документа и удалит его из каталога и из перечня полок
    '''
    number = input('Введите номер документа: ')
    sh = find_doc_in_directories(number)
    if sh is None:
        print('Документ не найден')
        return

    directories[sh].remove(number)
    for doc in documents:
        if doc['number'] == number:
            documents.remove(doc)
            break
    print('Удалено')


def move():
    '''
    спросит номер документа и целевую полку и переместит его с текущей полки на целевую
    '''
    number = input('Введите номер документа: ')
    sh = find_doc_in_directories(number)
    if sh is None:
        print('Документ не найден')
        return

    target_shelf = input('Введите целевую полку: ')
    if target_shelf not in directories:
        print('Нет такой полки')
        return
    if sh == target_shelf:
        print('Документ уже на полке')
        return
    directories[sh].remove(number)
    directories[target_shelf].append(number)
    print('Перемещено')


def add_shelf():
    '''
    спросит номер новой полки и добавит ее в перечень
    '''
    new_shelf = input('Введите номер новой полки: ')
    if not new_shelf.isdigit():
        print('Номер полки должен быть числом')
        return
    if new_shelf in directories:
        print('Полка уже существует')
        return
    directories[new_shelf] = []
    print('Добавлено')


def exit():
    '''
    выход из программы
    '''
    import sys
    sys.exit()


commands = {
    'p': people,
    'pa': people_all,
    'l': list_docs,
    's': shelf,
    'a': add,
    'd': delete,
    'm': move,
    'as': add_shelf,
    'e': exit
}

if __name__ == '__main__':
    for cmd, fn in commands.items():
        print(cmd, '\t', fn.__doc__.strip())

    while True:
        print()  # вывод пустой строки для лучшего отображения
        cmd = input('Введите команду: ')
        if cmd in commands:
            commands[cmd]()
        else:
            print('Неизвестная команда')