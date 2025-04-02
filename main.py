from stats import get_num_words, sort_char_list, get_num_character
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    path = sys.argv[1]
    text = get_book_text(path)
    number_words = get_num_words(text)
    char_number = get_num_character(text)
    sorted_dict = sort_char_list(char_number)

    #Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzig book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")

    #Print each character and its count
    for char_dict in sorted_dict:
        char = char_dict["char"]
        count = char_dict["count"]

        #only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ================")

main()