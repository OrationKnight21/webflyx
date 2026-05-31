from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

#function acting as a helper function which returns the value of num from the first dictionary.
def sort_on(item:CharacterCount):
    return item["num"]

#function to print the character count as desired i.e. in a reversed order.
def sorted_list(char_dict)->list[CharacterCount]:
    list_1 = []
    for char,count in char_dict.items() :
        list_1.append({"char":char,"num":count})
    list_1.sort(reverse=True,key=sort_on)
    return list_1

#the function below uses .read() to read the contents of the file. A demo function.
def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents 

#the function below returns the total number of words from the file.
def number_of_words(path_to_file) -> int:
    with open(path_to_file) as f:
        file_contents =  f.read()
        num = file_contents.split()
    return len(num)

#function to count each character's appearance in the whole book
def count_character(text_content) -> dict[str:int]:
    all_characters = text_content.lower()
    dictionary = {}
    for char in all_characters:
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char]=1
    return dictionary