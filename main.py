from stats import get_word_count, get_symbol_count, sort_on, sorted_char_list, get_book_text
import sys

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_symbol_count(text)
    sorted_chars = sorted_char_list(char_count)

    print_report(book_path, word_count, sorted_chars)

def print_report(path, words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {words} total words")
    print("--------- Character Count -------")

    for ch in chars:
        if not ch['char'].isalpha():
            continue
        print(f"{ch['char']}: {ch['num']}") 

    print (f"--- End report ---")

main()