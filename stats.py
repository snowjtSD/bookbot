def num_words(file_text):
    word_list = file_text.split()
    num_words = 0
    for i in word_list:
        num_words += 1
    return print(f"{num_words} words found in the document")


def letter_count(file_text):
    letter_dict = {}
    word_list = file_text.split()
    for word in word_list:
        word = word.lower()
        for i in word:
            if i in letter_dict:
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1
    print(letter_dict)
