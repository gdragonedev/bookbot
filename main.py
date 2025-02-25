import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
from stats import (
    count_words,
    get_chars_dict,
    sort_char_dict
)

def main():
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = get_chars_dict(text)
    char_sorted_list = sort_char_dict(chars_dict)
    print_report(book_path, num_words, char_sorted_list)

def get_book_text(book_fp):
    with open(book_fp, 'r') as book_file:
        return book_file.read()

def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for item in char_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()