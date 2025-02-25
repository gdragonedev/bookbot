def count_words(book_text):
    return len(book_text.split())

def get_chars_dict(book_text):
    char_dict = {}
    book_lower = book_text.lower()

    for char in book_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_dict(char_dict):
    chars_list = []
    for char in char_dict:
        if char.isalpha():
            chars_list.append({"char": char, "num": char_dict[char]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(char_dict):
    return char_dict["num"]