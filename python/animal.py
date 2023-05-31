from excep import excep as ex
import csv
import export as exp
import inport as imp


class animal:
    # добавить животное
    def add_animal(path,x):
        try:
            ls = ex.input_data(x)
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

    # редактирование 
    def change_commands(path, x):
        index_list = []
        list_note = exp.read_data(path)
        search_filter = ex.check_input_string('Ваши данные: ')
        i = 0
        for note in list_note:
            if search_filter == note[x] in note:
                index = list_note.index(note)
                print(i, ". ", list_note[index])
                index_list.append(index)
                i = i+1
            
        if len(index_list) == 1:
            ls= ex.filter_for_commands()
            print(f'Добавлена команда "{ls}".')
            if note[3] == '-':
                ls1 =[note[0],note[1], note[2], ls]
            else:
                # note[3] = "{note[3]} , {ls}"
                # ls2 = f"[{ls}, {note[3]}]"
                ls1 =[note[0], note[1], note[2], f"{note[3]} {ls}"]
            list_note.pop(index)
            list_note.insert(index, ls1)
            imp.rewrite_csv(list_note, path, 'w')
            return
        elif len(index_list) > 1:
            i = ex.digit(len(index_list))
            ls= ex.filter_for_commands()
            print(f'Добавлена команда "{ls}".')
            if note[3] == '-':
                ls1 =[note[0],note[1], note[2], ls]
            else:
                # ls2 = f"[{ls}, {note[3]}]"
                ls1 =[note[0],note[1], note[2],f"{note[3]} {ls}"]
            list_note.pop(index)
            list_note.insert(index, ls1)
            imp.rewrite_csv(list_note, path, 'w')
            return
        else:
            print('По этим данным "{}" ничего не найдено.'.format(search_filter))

    