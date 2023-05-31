from logg import logg
import sys
import os
from user_interface import user_interface as ui



class excep:
    def action(desc: str):
        while(True):
            i = input('Введите {}: '.format(desc)) 
            if i.isdigit():
                logg.entered_logger(i)
                return i
            print("Это не корректный ввод")
            text = "Пользователь ввел: " + i + ". Это некорректный ввод"
            logg.actions_logger(text)
    
        # ввод данных пользователем
    def input_data(x):
        id = x
        # id = Excep.action("ID: ")
        name = excep.check_input_string('Имя: ')
        ui.choice_type_menu()
        kind=ui.choice_type(excep.digit(6))
        commands = '-'
        return [id, name, kind, commands]

# ввод данных и проверка строковых данных(оптимизация кода)
    def check_input_string(desc: str):
        try:
            while True:
                val = input('Введите {}: '.format(desc))
                if len(val) < 1: # or not val.isalpha():
                    print('Поле "{}" должно быть не пустым.'.format(desc))
                    logg.actions_logger ('Пользователь ввел некорректные данные')
                    continue
                return val
        except Exception:
            print(Exception)
    
    def digit(x):
        try:
            while(True):
                i = input("Введите выбранный пункт: ")
                if i.isdigit():
                    i = int(i)
                    if i < x+1:
                        logg.entered_logger(i)
                        return i
                    else: 
                        print("Вам надо ввести число из диапазон")
                        continue
                print("Вам надо ввести число")
                text = "Пользователь ввел: " + i + ". Это некорректный ввод"
                logg.actions_logger(text)
        except Exception:
            print(Exception)

    def read_file_except(file_path):
        if not os.path.exists(file_path):
            print(f'Файл не найден или некорректно указан путь: {file_path}')
            sys.exit()
    
    def filter_for_commands():
        ui.commands()
        x = excep.digit(6)
        if x == 1:
            return 'Сидеть'
        elif x == 2:
            return 'Лежать'
        elif x == 3:
            return 'Рядом'
        elif x == 4:
            return 'Прыгать'
        elif x == 5:
            return 'Можно'
        else:
            return 'Нельзя'

