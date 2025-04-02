def get_num_words(words):
    counter = 0
    number_of_words = words.split()
    for word in number_of_words:
        counter += 1
    return counter

def get_num_character(text):
    unique_chars = text.lower()

    char_counts = {}

    for char in unique_chars:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_list(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list