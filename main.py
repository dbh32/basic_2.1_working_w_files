def get_shop_list_by_dishes(dishes, person_count):
    '''Функция по Задаче №2'''
    result = {}
    for dish in dishes:
        if dish in cook_book.keys():
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient['quantity'] = int(ingredient['quantity']) * person_count
                if ingredient['ingredient_name'] not in result.keys():
                    result[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'],
                                                             'measure': ingredient['measure']}
                else:
                    d1 = result[ingredient['ingredient_name']]
                    d2 = d1['quantity'] + ingredient['quantity']
                    d1.update({'quantity': d2})
                    # вспомогательные переменные
    # print(result)
    # Задача №2
    # Запуск функции на 53 строке


def create_dish():
    '''Создание списков под каждое блюдо'''
    dish = []
    count = int(f.readline().strip())
    cycle = 0
    while cycle != count:
        cycle += 1
        dish.append(create_ingredients())
    f.readline().strip()
    return dish


def create_ingredients():
    '''Наполняем списки блюд ингридиентами'''
    l1 = f.readline().strip()
    l2 = l1.split(' | ', 3)
    # вспомогательные переменные
    ingredients = {'ingredient_name': l2[0],
                   'quantity': l2[1],
                   'measure': l2[2]}
    return ingredients


with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        line = line.strip()
        cook_book[line] = create_dish()
    # print(cook_book)
    # Задача №1

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
