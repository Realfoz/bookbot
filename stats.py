import string


def get_num_words(text):
    num_words = text.split() 
    return len(num_words)

def name_search(text):
    split_words = text.lower().split()
    clean_words = [word.strip(string.punctuation) for word in split_words] 
    name_list = ["victor", "igor", "elizabeth"]
    name_counts = {name: clean_words.count(name) for name in name_list}
    return name_counts
         


def letter_count(text):
    letters = {}
    lower_case = text.lower()
    for char in lower_case:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1          
    return(letters)


def sort_dic(dict):
    sorted_char_list = []
    for char, count in dict.items():
        char_dict = {"char": char, "count":count}
        sorted_char_list.append(char_dict)
        sorted_char_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_char_list



