cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

with open('cook_book.txt', 'w') as file:
    for dish in cook_book:
        file.write(dish + '\n' + str(len(cook_book[dish])) + '\n')
        for line in cook_book[dish]:
            file.write(f"{line['ingredient_name']} | {line['quantity']} | {line['measure']} \n")
        file.write('\n')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book:
        for line in cook_book[dish]:
            if line['ingredient_name'] in shop_list:
                shop_list[line['ingredient_name']] = {'measure': line['measure'],
                'quantity': line['quantity'] * person_count + shop_list[line['ingredient_name']]['quantity']}
            elif dish in dishes:
                shop_list.setdefault(line['ingredient_name'],
                {'measure':line['measure'], 'quantity':line['quantity'] * person_count})
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open('1.txt') as f1:
    with open('2.txt') as f2:
        with open('3.txt') as f3:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            lines3 = f3.readlines()
            all_files = [[len(lines1), '1.txt', lines1], [len(lines2), '2.txt', lines2], [len(lines3), '3.txt', lines3]]
            all_files.sort(key=lambda x: x[0])
            with open('all.txt', 'w') as all:
                for file in all_files:
                    all.write(f"{file[1]} \n")
                    all.write(f"{file[0]} \n")
                    all.write(f"{''.join(file[2])} \n \n")