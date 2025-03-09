def get_num_words(text):
    num_words = text.split()
    return len(num_words)



def letter_count(text):
    letters = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1          
    return(letters)

 