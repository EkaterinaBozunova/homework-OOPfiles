import os
import time
from pprint import pprint

def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list

def acounting(file:str) -> int:
    return sum(1 for _ in open(file, 'rt', encoding='utf-8'))

def rewrite_file(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a', encoding='utf-8')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f"{file_from_list[0]}\n")
        with open(file_from_list[1], 'r', encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


if __name__ == '__main__':
    file_for_writing = os.path.abspath('\\Users\\katri\\Desktop\\homework-OOPfiles\\rewrite_file.txt')
    base_path = os.getcwd()
    location = os.path.abspath('\\Users\\katri\\Desktop\\homework-OOPfiles\\files')
    cook_book = read_cookbook()
    print('Задание 1:')
    time.sleep(1)
    print(cook_book)
    print('Задание 2:')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))

    time.sleep(2)
    print('Задание 3:')
    
    rewrite_file(file_for_writing, base_path, location)