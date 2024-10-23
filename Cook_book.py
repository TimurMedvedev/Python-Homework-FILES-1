import os

def make_dict_of_recipes(text_path, cook_book):
    with open(text_path, encoding='utf-8') as f:
        recipes = f.readlines() 
    i=-1
    keys = []
    for line in recipes:
        words_in_line = line.split('|')
        if len(words_in_line) == 1 and words_in_line[0] != '\n':
            keys.append(words_in_line[0].strip())
            cook_book[words_in_line[0].strip()] = []
            i+=1
        elif len(words_in_line)>1:
            cook_book[keys[i]] += [{'ingredient_name': words_in_line[0], 'quantity': words_in_line[1], 'measure': words_in_line[2].strip()}]

def get_shop_list_by_dishes(dishes, person_count):
    list_of_ingridients = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                list_of_ingridients[i['ingredient_name']] = {'quantity': int(i['quantity'])*person_count, 'measure': i['measure']}      
    return list_of_ingridients


cook_book = {}
text_path = os.path.join(os.getcwd(), 'recipes.txt')
make_dict_of_recipes(text_path, cook_book)
print(cook_book)
dishes = ['Омлет', 'Фахитос']
print(get_shop_list_by_dishes(dishes, 2))


