def get_book_text(filepath): # takes filepath as input then outputs the contents as a string
    with open(filepath) as f:
        return f.read()
    

from stats import get_num_words
from stats import letter_count

def main():
    book_path = "/home/scott/projects/github.com/bootdotdev/bookbot/books/frankenstein.txt"
    full_text = (get_book_text(book_path)) # runs the get_book_text func with the book path provided
    words = (get_num_words(full_text)) # uses the get_num_words func with the full_text to count the total words
    letter_counter = (letter_count(full_text)) # uses the letter_count func with full_text to count each unique char
    print (F"{words} words found in the document")
    print (letter_counter)
      
main()