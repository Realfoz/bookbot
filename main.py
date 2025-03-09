def get_book_text(filepath): # takes filepath as input then outputs the contents as a string
    with open(filepath) as f:
        return f.read()
    

from stats import get_num_words, letter_count, sort_dic

def main():
    import sys
    if len(sys.argv) < 2:
        print("Error: Please provide a path to a book file.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Error: Too many arguments provided. Only one book argument is accepted.")
        sys.exit(1)
    book_path = sys.argv[1] 
    
    full_text = (get_book_text(book_path)) # runs the get_book_text func with the book path provided
    words = (get_num_words(full_text)) # uses the get_num_words func with the full_text to count the total words
    letter_counter = (letter_count(full_text)) # uses the letter_count func with full_text to count each unique char
    sorted_chars = sort_dic(letter_counter) # uses sorted_chars func to sort the dic values into reverse numerical order
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}")
    print ("----------- Word Count ----------")
    print (f"Found {words} total words")
    print ("--------- Character Count -------")
    for i in sorted_chars:
        character = i["char"] 
        count = i["count"]  
        print(f"{character}: {count}")
    print ("============= END ===============")

      
main()