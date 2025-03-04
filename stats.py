def num_words(file_text):
    word_list = file_text.split()
    num_words = 0
    for i in word_list:
        num_words += 1
    return print(f"{num_words} words found in the document")
