from excep import excep as ex
import csv
import export as exp
import inport as imp
from logg import logg
from pet.petType import *
from user_interface import user_interface as ui
from count import count



class add:
    def input_pet(x):
        try:
            id = x
            name = ex.check_input_string('Имя: ')
            colour = ex.check_input_string('Цвет: ')
            ui.choice_type_menu()
            kind=ex.digit(6)
            commands = '-'
            if x == 1:
                return dog(id, name, colour, commands)
            elif x == 2:
                return cat(id, name, colour, commands)
            elif x == 3:
                return hamster(id, name, colour, commands)
            elif x == 4:
                return horse(id, name, colour, commands)
            elif x == 5:
                return donkey(id, name, colour, commands)
            elif x == 6:
                return camel(id, name, colour, commands)

        except Exception:
            print('-'*50)
            print(Exception)


    def add_animal(path, x):
        try:
            ls = add.input_pet(x)
            with open(path, 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(ls)
        except Exception:
            print('-'*50)
            print("Mistake")
        else:
            print('-'*50)
            print(f'Новое животное было добавлено.Кол-во животных: {ls[0]}')
            print('-'*50)