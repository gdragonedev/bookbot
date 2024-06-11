file_path = "books/frankenstein.txt"

def main():
    print(f"--- Begin report of {file_path} ___\n")
    word_count(file_path)
    char_count_report(file_path)
    print("--- End report ---")

def read_file(path):
    with open(path) as file:    
        return file.read()

def word_count(path):
    words = read_file(path).split()
    print(f"{len(words)} words found in the document\n")

def character_count(path):
    char_counts = {}
    lower_text = read_file(path).lower()
    for char in lower_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def char_count_report(path):
    char_count_list = []
    char_count_dict = character_count(path)

    for key in char_count_dict:
        if key.isalpha():
            char_dict = {
                "char": key,
                "num" : char_count_dict[key]
            }
            char_count_list.append(char_dict)

    char_count_list.sort(reverse=True, key=sort_on)
    
    for dict in char_count_list:
        print(f"The character '{dict["char"]}' was found {dict["num"]} times")

def sort_on(dict):
    return dict["num"]

main()