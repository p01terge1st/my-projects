#!/usr/bin/python3   
#author: p01terge1st

'''
запись в файл:
'''
def file_save():
    try:
        with open (input('Название и путь файла куда сохранить:\n'), 'a') as file: #открываем куда писать полученные данные
            file.write('blabla') # записываем файл. Вместо 'blabla' можно указать переменную 
            print('Успешно сохранено.')
    except FileNotFoundError:
        print('Не могу найти указанный путь. Формат ввода: \'E:\passwords.txt\'')
        file_save()
    except PermissionError:
        print('Доступ в указанную папку(каталог) запрещен!\n')
        file_save()
file_save()
