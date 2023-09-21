def build_dict(text):
    if not text.strip():
        return {}
    text = text.replace(',', '')
    text = text.lower()
    words = text.split()
    dictionary = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in dictionary:
            dictionary[current_word] = [next_word]
        else:
            dictionary[current_word].append(next_word) #har vi en nyckel så kommer nästa ord att läggas till på nyckeln. Detta då vi har gjort en lista och ej ett dicitonary
    return dictionary

def most_common_words_finder(dictionary):
    if not dictionary:
        return {}

    maxvalue_of_following_word = 0
    for following_words in dictionary.values():
       if len(following_words) > maxvalue_of_following_word:
            maxvalue_of_following_word = len(following_words)

    most_common_words_dictionary = {}
    for word, following_words in dictionary.items():
        if len(following_words) == maxvalue_of_following_word:
            most_common_words_dictionary[word] = following_words
    return most_common_words_dictionary


def test_most_common_words_finder():
    print('\nTest of most_common_words_finder...:')

    dictionary = {'Du och du, och valfrid': {'du': ['och', 'och'], 'och': ['du', 'valfrid']},
                  'Du och du, och valfrid du hej': {'du': ['och', 'och', 'hej'], 'och': ['du', 'valfrid']},
                  ' ': { }}

    for case in dictionary:
        if most_common_words_finder(build_dict(case))!= dictionary[case]:
            print('Test failed for:', case, 'Exptected Outcome:', most_common_words_finder(build_dict(case)), 'But Got', dictionary[case])
        else:
            print('\n'+ case, 'became the dictionary:', most_common_words_finder(build_dict(case)))
    print('\nTest of most_common_words_finder completed!')
test_most_common_words_finder()