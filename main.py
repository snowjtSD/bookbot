def get_book_text(file_text):
    with open(file_text) as f:
        file_text = f.read()
        return file_text

def num_words(file_text):
    word_list = file_text.split()
    num_words = 0
    for i in word_list:
        num_words += 1
    print(f"{num_words} words found in the document")


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words(file_contents)

main()
