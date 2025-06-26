def get_book_text(path_to_file):
    """
    Reads the contents of a file and returns it as a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_word_number(path_to_file):
    """
    Counts the number of words in a book file.
    """
    book_content = get_book_text(path_to_file)
    total_words = book_content.split()
    return len(total_words)


def get_character_number(path_to_file):
    """
    Counts the number of characters in a book file (including whitespace and symbols).
    """
    book_content = get_book_text(path_to_file)
    bc_uniform = book_content.lower()

    return len(bc_uniform)


def get_character_counts(path_to_file):
    """
    Returns a dictionary with each character as key and its count as value.
    """
    book_content = get_book_text(path_to_file)
    bc_uniform = book_content.lower()

    char_counts = {}
    for char in bc_uniform:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_on(items):
    return items["num"]


def sorted_list_char_dicts(char_counts_dict):
    """
    Reurns a sorted list of distionary items by count in ascending order.
    """
    res_list = []
    for char, count in char_counts_dict.items():
        res_dict = {"char": char, "num": count}
        res_list.append(res_dict)

    sorted_result = res_list.sort(reverse=True, key=sort_on)

    return sorted_result
