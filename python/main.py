from user_interface import user_interface as console
from excep import excep as ex
from animal import animal
import export as exp
from pet.add import *


path = 'animal.csv'

def main(path):
    console.main_menu("Welcome")
    while(True):
        console.main_menu("Menu")
        i = ex.action("пункт")
        match i:
            case "1": 
                print('-'*50)
                print('Вы выбрали "Добавить животное"')
                print('-'*50)
                animal.add_animal(path,1)
                # add.add_animal(path, 1)
               
            case "2":
                console.choice_commands()
                i = ex.action("пункт")
                if i == "1":
                    print('-'*50)
                    print('Вы выбрали "Вывод всех доступных команд"')
                    print('-'*50)
                    console.commands()
                    # print('-'*50)
                    # print('Вывод всего"')
                    # print('-'*50)
                    # exp.show_all(path)


                elif i == "2": 
                    print('-'*50)
                    print('Вы выбрали " Вывод команд у определенного животного"')
                    print('-'*50)
                    exp.show_all(path)
                    print('-'*50)
                    x = exp.selected_filter()
                    exp.show_selected_note(path, x)
                    


                elif i == "3": 
                    print('-'*50)
                    print('Вы выбрали "Обучить животное команде"')
                    print('-'*50)
                    i =  exp.selected_filter()
                    animal.change_commands(path,i)

                elif i == "4":
                    print('-'*50)
                    print("Программа завершила работу")
                    print('-'*50)
                    break
                else:
                    print('-'*50)
                    print("Вы ввели неправильные данные")
                    print('-'*50)

            case "3":
                print('-'*50)
                print("Программа завершила работу")
                print('-'*50)
                break
            case _: 
                print('-'*50)
                print("Не корректный ввод")

main(path)