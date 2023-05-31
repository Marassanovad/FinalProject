import export as exp

class count:
    # global counter

    
    def add_counter(path):
        try:
            list_note = exp.read_data(path)
            counter = 0
            for note in list_note:
                counter = counter + 1
            return counter
        except Exception:
            print('Mistake')
        # else:
        #     print('ID был записан')
        