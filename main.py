def get_book_text(filepath): # takes filepath as input then outputs the contents as a string
    with open(filepath) as f:
        return f.read()
    

def get_num_words(text):
    num_words = text.split()
    return len(num_words)


def main():
    book_path = "/home/scott/projects/github.com/bootdotdev/bookbot/books/frankenstein.txt"
    full_text = (get_book_text(book_path)) # runs the get_book_text func with the book path provided
    words = (get_num_words(full_text))
    print (F"{words} words found in the document")
      
main()


