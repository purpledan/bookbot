from stats import count_words
from stats import count_chars
from stats import report

import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
   
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    word_count = count_words(book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count = count_chars(book) 
    print("--------- Character Count -------")
    char_sorted = report(char_count)
    for entry in char_sorted:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    return

main()
