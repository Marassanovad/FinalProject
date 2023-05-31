from dataclasses import dataclass, field

class pet():
    id: int
    name: str
    colour: str
    commands: list

def print_pet(pet):
    print(f'Id: {pet.id}')
    print(f'Имя: {pet.name}')
    print(f'Цвет: {pet.colour}')
    print('Команды: ')
    i = 1
    for command in pet.commands:
        print(' '*2 + i + ". " + command)
        i= i + 1

    # print(f'Команды: {pet.commands}')