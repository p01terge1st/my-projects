import itertools, random

simbols = input("Введи предполагаемые символы:\n")
lenght = input('Введите количество символов:\n')
brut_file = []

def file_save(data_file): # сохранение в файл..
    try:
        with open (input('Название и путь файла куда сохранить:\n***Например f:/filename.txt***\n'), 'a') as file: #открываем куда писать полученные данные
            file.write(data_file) # записываем данные в файл
            print('Успешно сохранено.')
    except FileNotFoundError:
        print('Не могу найти указанный путь. Формат ввода: \'E:\passwords.txt\'')
        file_save(data_file)
    except PermissionError:
        print('Доступ в указанную папку(каталог) запрещен!\n')
        file_save(data_file)


def pass_gen(simbols, lenght, brut_file):
    words = itertools.product(simbols, repeat = int(lenght)) # генерация паролей
    for i in words: #создание списка
        words = (''.join(i))
        brut_file.append(words) #запись полученных слов в список в brut_file
    random.shuffle(brut_file) # перемешиваем список
    brut_file = "\n".join(brut_file) #каждый пароль на новой строке
    file_save(brut_file)


pass_gen(simbols, lenght, brut_file)