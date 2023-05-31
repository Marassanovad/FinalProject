import csv
from excep import excep as ex
from user_interface import user_interface as console


def read_data(path): #Функция, читает данные из файла в список
    
    ex.read_file_except(path)
    with open(path, "r") as file:
        reader = csv.reader(file)
        data_list = []
        for row in reader:
            data_list.append(row)
        return data_list
			

def show_all(path): #Функция, выводит все заметки из указанного .csv файла.

	list_ = read_data(path)
	
	print('''\t ID ||   Имя   ||   Вид   ''')
	print('=' * 50)
	for note in list_:
		print(f'\t {note[0]}. ||   {note[1]}  ||   {note[2]} \n \n      Список изученных команд: {note[3]}' )
	print('=' * 50)


def selected_filter():
    while (True):
        console.choise_search_filter()
        k = ex.action('пункт')
        if k == "1":  
            print('-'*50)
            print('Вы выбрали "По идентификатору"')
            print('-'*50)
            return 0
            # show_selected_note(path, 0)

        elif k == "2": 
            print('-'*50)
            print('Вы выбрали "По имени"')
            print('-'*50)
            return 1
            # show_selected_note(path, 1)
                    
        elif k == "3": 
            print('-'*50)
            print('Вы выбрали "По виду"')
            print('-'*50)
            return 2
            # show_selected_note(path, 2)        

        elif k == "4":
            print('-'*50)
            print("Производиться выход в главное меню")
            print('-'*50)
            break
                     
        else:
            print('-'*50)
            print("Вы ввели неправильные данные")
            print('-'*50)

def show_selected_note(path, x):
	'''
	Функция, выводит информацию о заметках по указанным данным
	'''
    
	list_note = read_data(path)
	search_filter = ex.check_input_string('Введите параметры поиска: ')
	for note in list_note:
		if search_filter == note[x] in note:
			index = list_note.index(note)
			print(list_note[index])
            

        
           