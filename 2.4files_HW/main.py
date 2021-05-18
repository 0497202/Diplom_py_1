# coding=utf-8
with open('recipes.txt', 'r') as file:
    data = file.read()
    print(data)

cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        ingrid_count = f.readline().strip()
        for _ in range(int(ingrid_count)):
            ingrid_list = f.readline().strip().split(" | ")
            if dish_name not in cook_book.keys():
                cook_book[dish_name] = [{'ingredient_name': ingrid_list[0],
                                         'quantity': ingrid_list[1], 'measure': ingrid_list[2]}]
            else:
                cook_book[dish_name].append({'ingredient_name': ingrid_list[0],
                                             'quantity': ingrid_list[1], 'measure': ingrid_list[2]})
        f.readline()

print(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    result_dict = {}
    for dish in dishes:
        # print(dish)
        for (key, value) in cook_book.items():
            if dish == key:
                for entry in value:
                    k = (entry["ingredient_name"]).strip()
                    l = (entry["measure"]).strip()
                    m = int((entry["quantity"]).strip())
                    if k in result_dict.keys():
                        result_dict[k]["quantity"] = m * person_count + (result_dict[k]['quantity'])
                    else:
                        result_dict[k] = {"measure": l, "quantity": m * person_count}
    print(result_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


from pprint import pprint


def text_sort_by_line():

    cooment_text = {}

    with open('1.txt', encoding='UTF-8') as t1:
        text1 = t1.readlines()
        cooment_text[len(text1)] = ['1.txt', text1]

    with open('2.txt', encoding='UTF-8') as t2:
        text2 = t2.readlines()
        cooment_text[len(text2)] = ['2.txt', text2]

    with open('3.txt', encoding='UTF-8') as t3:
        text3 = t3.readlines()
        cooment_text[len(text3)] = ['3.txt', text3]

    with open('union_text.txt', 'a', encoding='UTF-8') as union:
        list_long = list(cooment_text.keys())
        list_long.sort()
        for i in list_long:
            union.write(f'{cooment_text[i][0]}\n')
            union.write(f'{str(i)}\n')
            union.write(f'{"".join(cooment_text[i][1])}\n')

    return

text_sort_by_line()