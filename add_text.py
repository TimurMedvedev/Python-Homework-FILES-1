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


text1_path = os.path.join(os.getcwd(), '1.txt')
text2_path = os.path.join(os.getcwd(), '2.txt')
text3_path = os.path.join(os.getcwd(), '3.txt')

text1 = [['\n1.txt\n'], [str(len(add_file_to_list(text1_path)))+ '\n'], add_file_to_list(text1_path)]
text2 = [['\n2.txt\n'], [str(len(add_file_to_list(text2_path)))+ '\n'], add_file_to_list(text2_path)]
text3 = [['\n3.txt\n'], [str(len(add_file_to_list(text3_path)))+ '\n'], add_file_to_list(text3_path)]

text_dict = {len(add_file_to_list(text1_path)): text1, 
             len(add_file_to_list(text2_path)): text2, 
             len(add_file_to_list(text3_path)): text3
             }
sorted_text_dict = dict(sorted(text_dict.items()))

add_lists_to_file(sorted_text_dict, 'sorted_text.txt')
