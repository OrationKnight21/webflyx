from stats import *
import sys
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_test(path)
    total_words = number_of_words(path)
    char_count = count_character(file_contents)
    print(f"Found {total_words} total words")
    #print(char_count)
    sorted_char_count = sorted_list(char_count)
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

main()
