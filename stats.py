

def get_book_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_dict = {}
    for char in text:
        
        if char.lower() in char_dict.keys():
            char_dict[char.lower()]+=1
        else:
            char_dict[char.lower()] = 1

    return char_dict

def split_to_list_of_dicts(dict):
    list_of_dicts=[]
    for key, value in dict.items():
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = value
        list_of_dicts.append(new_dict)
    return list_of_dicts


def sort_on(items):
    return items["num"]