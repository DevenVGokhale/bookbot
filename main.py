from stats import get_word_number, get_character_counts, sort_on, sorted_list_char_dicts
import sys

if len(sys.argv) < 2:
    print(
        "Usage: python3 main.py <path_to_book>. Did you forget to provide the path to the book?"
    )
    sys.exit(1)

book_path = sys.argv[1]


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_word_number(book_path)
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    char_counts = get_character_counts(book_path)
    print("\nCharacter counts:")
    for char, count in char_counts.items():
        if char.isalpha():
            print(f"{char}: {count}")


main()
