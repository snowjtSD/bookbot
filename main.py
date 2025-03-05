from stats import num_words
from stats import letter_count
from stats import sort_dict

def get_book_text(file_text):
    with open(file_text) as f:
        file_text = f.read()
        return file_text

def sort_on(dict):
    return dict[i]

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    words = num_words(file_contents)
    letters = letter_count(file_contents)
    sorted_list_dict = sort_dict(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for element in sorted_list_dict:
        print(f"{element['name']}: {element['num']}")
    print("============= END ===============")
main()
