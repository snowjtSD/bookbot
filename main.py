def get_book_text(file_text):
    with open(file_text) as f:
        file_text = f.read()
        print(file_text)
        return file_text

def main():
    get_book_text("books/frankenstein.txt")


main()
