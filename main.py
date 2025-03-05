from stats import num_words
from stats import letter_count

def get_book_text(file_text):
    with open(file_text) as f:
        file_text = f.read()
        return file_text

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words(file_contents)
    letter_count(file_contents)

main()
