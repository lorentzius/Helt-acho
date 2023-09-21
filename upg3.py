import random

import random

def build_dict(text):
    if not text.strip():
        return {}
    words = text.split()
    word_dictionary = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in word_dictionary:
            word_dictionary[current_word] = [next_word]
        else:
            word_dictionary[current_word].append(next_word)
    return word_dictionary

def dictionary_random_key_chooser(dictionary, length):
    if not dictionary:
        return "ERROR: No dictionary"
    random_key = random.choice(list(dictionary.keys()))
    new_text = random_key[0].upper() + random_key[1:]
    while len(new_text.split()) < length and random_key in dictionary and dictionary[random_key]:
        random_value = random.choice(dictionary[random_key])
        new_text += " " + random_value
        random_key = random_value
    if not new_text.endswith("."):
        new_text += "."
    return new_text

def read_file(file):
    text = open('list1.txt').read()
    return text

dictionary = build_dict(read_file('list1.txt'))
length = int(input("Approximately how long should the new generated text be: "))
result = dictionary_random_key_chooser(dictionary, length)

print(result)



















