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

def sort_on(d):
    return d["num"]


def sorted_char_list(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()