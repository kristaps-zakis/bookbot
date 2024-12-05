def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_symbol_count(text)
    sorted_chars = sorted_char_list(char_count)

    print_report(book_path, word_count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_word_count(text):
    return len(text.split())

def get_symbol_count(text):
    text = text.lower()
    symbol_directory = {}

    for char in text:
        if char not in symbol_directory:
            symbol_directory[char] = 1
        else:
            symbol_directory[char] += 1

    return symbol_directory

def print_report(path, words, chars):
    print (f"--- Begin report of {path} ---")
    print (f"{words} words found in the document")
    print()

    for ch in chars:
        if not ch['char'].isalpha():
            continue
        print(f"The '{ch['char']}' character was found {ch['num']} times") 

    print (f"--- End report ---")

def sort_on(d):
    return d["num"]

def sorted_char_list(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

main()