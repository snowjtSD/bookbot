def num_words(file_text):
    word_list = file_text.split()
    num_words = 0
    for i in word_list:
        num_words += 1
    return num_words

def letter_count(file_text):
    letter_dict = {}
    word_list = file_text.split()
    for word in word_list:
        word = word.lower()
        for char in word:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict

def sort_on(dict):
    return dict['num']

def sort_dict(some_dict):
    sorted_list = []
    for i in some_dict:
        sorted_list.append(dict(name=i, num=some_dict[i]))
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
