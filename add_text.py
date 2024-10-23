import os

def add_file_to_list(text):
    with open(text, encoding='utf-8') as f:
        list_of_lines = f.readlines()
    return list_of_lines

def add_lists_to_file(lists, sorted_text):
    with open(sorted_text,'w', encoding='utf-8') as f:
        for key in lists:
            for row in lists[key]:
                for element in row:
                    f.writelines(element)

def make_text_list(directory):
    texts_path = []
    for text in directory:
        texts_path.append(os.path.join(os.getcwd(),'Part 3', text))
    texts_dict = {}
    for i, path in enumerate(texts_path):
        texts_dict[len(add_file_to_list(path))] = [[f'\n{directory[i]}\n'], [str(len(add_file_to_list(path)))+ '\n'], add_file_to_list(path)]
    return texts_dict


texts_directory = os.listdir(os.path.join(os.getcwd(), 'Part 3'))
make_text_list(texts_directory)
sorted_text_dict = dict(sorted(make_text_list(texts_directory).items()))
add_lists_to_file(sorted_text_dict, 'sorted_text.txt')
