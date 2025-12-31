
from stats import get_book_words, get_char_count, split_to_list_of_dicts, sort_on
import sys

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    get_book_text(path)
    book_text = get_book_text(path)
    book_words = get_book_words(book_text)
    
    char_count = get_char_count(book_text)
    #print(char_count)

    split_list_of_dicts = split_to_list_of_dicts(char_count)
    split_list_of_dicts.sort(reverse=True, key=sort_on)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------""")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for dict in split_list_of_dicts:
        if dict["name"].isalpha():
            print(f"{dict['name']}: {dict['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()



main()

