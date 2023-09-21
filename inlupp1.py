def read_file(file):
    if not file:
        return None
    try:
        with open(file) as f:
            text = f.read()
    except FileNotFoundError:
        return None
    if len(text.strip())==0:
        return None

    return text

def test_read_file():
    print('\nTest of read_file...')

    dictionary = {"list.txt": "HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJDA",
                  "list1.txt": None,
                  "no_file.txt": None}

    for case in dictionary:
       if read_file(case) != dictionary[case]:
           print('Test failed for', case, 'Expected', dictionary[case], 'but got', read_file(case))
    print(f'Test of read_file completed')
test_read_file()


def lower_case_maker(str):
    lower_case_string = str.lower()
    return lower_case_string

def test_lower_case_maker():
    print('\nTest of lower_case_maker...')

    dictionary = {
        "HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJ HEJDÅ": "hej jag heter nikita, och rickard anner hej hejdå",
        " ": " ",
        "HeJ": "hej",
        "123": "123"}

    for case in dictionary:
        if lower_case_maker(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', lower_case_maker(case), 'but got', dictionary[case])
    print(f'Test of lower_case_maker completed')
test_lower_case_maker()

def convert_to_list(str):
    list = str.split()
    return list

def test_convert_to_list():
    print('\nTest of convert_to_list...')

    dictionary = {
        "HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJ HEJDÅ": ['HEJ', 'JAG', 'HETER', 'NIKITA,', 'OCH', 'RICKARD', 'ANNER', 'HEJ', 'HEJDÅ'],
        " ": [],
        "HEJ": ['HEJ'],
        "123": ['123']}

    for case in dictionary:
        if convert_to_list(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', convert_to_list(case), 'but got', dictionary[case])
    print(f'Test of convert_to_list completed')
test_convert_to_list()

def string_cleaner(str):
    cleaned_string = ""
    for character in str:
        if character.isalpha() or character.isspace(): #character is space lägger till space
            cleaned_string += character
    return cleaned_string

def test_string_cleaner():
    print('\nTest of string_cleaner...')

    dictionary = {"HEJ JAG H3T3R N1K1T4, OCH RICK4RD ANN3R HEJ HEJDÅ": "HEJ JAG HTR NKT OCH RICKRD ANNR HEJ HEJDÅ",
                  " ": " ",
                  "HEJ": "HEJ",
                  "123": ""}

    for case in dictionary:
        if string_cleaner(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', string_cleaner(case), 'but got', dictionary[case])
    print(f'Test of string_cleaner completed')
test_string_cleaner()

def count_words(str):
    list = str.split()
    count = 0
    for word in list:
        count += 1
    return count

def test_count_words():
    print('\nTest of count_words...')

    dictionary = {"HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJ HEJDÅ": 9,
                  " ": 0,
                  "HEJ": 1,
                  "123": 1}

    for case in dictionary:
        if count_words(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', count_words(case), 'but got', dictionary[case])
    print(f'Test of count_words completed')
test_count_words()

def dictionary_maker(str):
    list = str.split()
    new_dictionary = dict.fromkeys(list, 0)
    return new_dictionary

def test_dictionary_maker():
    print('\nTest of dictionary...')

    dictionary = {
        "HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJ HEJDÅ": {'HEJ': 0, 'JAG': 0, 'HETER': 0, 'NIKITA,': 0, 'OCH': 0,  'RICKARD': 0, 'ANNER': 0, 'HEJDÅ': 0},
        " ": {},
        "HEJ": {'HEJ': 0},
        "123": {'123': 0}}

    for case in dictionary:
        if dictionary_maker(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', dictionary_maker(case), 'but got', dictionary[case])
    print(f'Test of dictionary completed')
test_dictionary_maker()

def dictionary_count(dict):
    length = len(dict)
    return length

def test_dictionary_count():
    print('\nTest of dictionary_count...')

    dictionary_1 = {'HEJ': 0, 'JAG': 0, 'HETER': 0, 'NIKITA': 0, 'OCH': 0, 'RICKARD': 0, 'ANNER': 0, 'HEJDÅ': 0}
    dictionary_2 = {}
    dictionary_3 = {'HEJ': 0}
    dictionary_4 = {'123': 0}

    expected_length1 = 8
    expected_length2 = 0
    expected_length3 = 1
    expected_length4 = 1 #vi måste ha på detta sätt då vi inte kan sätta en dictionary som expected då vi inte kan sätta nycklar som exptected.

    if dictionary_count(dictionary_1) != expected_length1:
        print('Test failed for', dictionary_1, 'Expected', expected_length1, 'but got', dictionary_count(dictionary_1))
    if dictionary_count(dictionary_2) != expected_length2:
        print('Test failed for', dictionary_2, 'Expected', expected_length2, 'but got', dictionary_count(dictionary_2))
    if dictionary_count(dictionary_3) != expected_length3:
        print('Test failed for', dictionary_3, 'Expected', expected_length3, 'but got', dictionary_count(dictionary_3))
    if dictionary_count(dictionary_4) != expected_length4:
        print('Test failed for', dictionary_4, 'Expected', expected_length4, 'but got', dictionary_count(dictionary_4))
    print(f'Test of dictionary_count completed')
test_dictionary_count()

def dictionary_value_of_keys(str):
    list = str.upper().split()
    new_dict = dict.fromkeys(list, 0)
    for word in list:
        if word in new_dict:
            new_dict[word] += 1
    return new_dict

def test_dictionary_value_of_keys():
    print('\nTest of dictionary_value_of_keys...')

    dictionary = {"HEJ JAG HETER NIKITA, OCH RICKARD ANNER HEJ HEJDÅ": {'HEJ': 2, 'JAG': 1, 'HETER': 1, 'NIKITA,': 1, 'OCH': 1, 'RICKARD': 1, 'ANNER': 1, 'HEJDÅ': 1},
                  " ": { },
                  "HEJ hej HEJ": {'HEJ': 3},
                  "123": {'123': 1}
                  }
    for case in dictionary:
        if dictionary_value_of_keys(case) != dictionary[case]:
            print('Test failed for', case, 'Expected', dictionary_value_of_keys(case), 'but got', dictionary[case])
    print(f'Test of dictionary_value_of_keys completed')
test_dictionary_value_of_keys()

def dictionary_keymax(dict):
    if not dict:
        return None
    keymax = max(dict, key=dict.get)
    return keymax

def test_dictionary_keymax():
    print('\nTest of dictionary_keymax...')

    dictionary1 = {'HEJ': 2, 'JAG': 1, 'HETER': 1, 'NIKITA,': 1, 'OCH': 1, 'RICKARD': 1, 'ANNER': 1, 'HEJDÅ': 1}
    dictionary2 = {}
    dictionary3 = {'HEJ': 2, 'JAG': 2}
    dictionary4 = {'123': 1}

    expected_keymax1 = 'HEJ'
    expected_keymax2 = None
    expected_keymax3 = 'HEJ'
    expected_keymax4 = '123'

    if dictionary_keymax(dictionary1) != expected_keymax1:
        print('Test failed for', dictionary1, 'Expected', expected_keymax1, 'but got', dictionary_keymax(dictionary1))
    if dictionary_keymax(dictionary2) != expected_keymax2:
        print('Test failed for', dictionary2, 'Expected', expected_keymax2, 'but got', dictionary_keymax(dictionary2))
    if dictionary_keymax(dictionary3) != expected_keymax3:
        print('Test failed for', dictionary3, 'Expected', expected_keymax3, 'but got', dictionary_keymax(dictionary3))
    if dictionary_keymax(dictionary4) != expected_keymax4:
        print('Test failed for', dictionary4, 'Expected', expected_keymax4, 'but got', dictionary_keymax(dictionary4))
    print(f'Test of dictionary_keymax completed')
test_dictionary_keymax()

def dictionary_keymax_count(dict):
    if not dict:
        return None
    keymax_count = dict[max(dict, key=dict.get)]
    return keymax_count

def test_dictionary_keymax_count():
    print('\nTest of dictionary_keymax...')

    dictionary1 = {'HEJ': 2, 'JAG': 1, 'HETER': 1, 'NIKITA,': 1, 'OCH': 1, 'RICKARD': 1, 'ANNER': 1, 'HEJDÅ': 1}
    dictionary2 = {}
    dictionary3 = {'HEJ': 2, 'JAG': 2}
    dictionary4 = {'123': 1}

    expected_keymax1 = 2
    expected_keymax2 = None
    expected_keymax3 = 2
    expected_keymax4 = 1

    if dictionary_keymax_count(dictionary1) != expected_keymax1:
        print('Test failed for', dictionary1, 'Expected', expected_keymax1, 'but got', dictionary_keymax(dictionary1))
    if dictionary_keymax_count(dictionary2) != expected_keymax2:
        print('Test failed for', dictionary2, 'Expected', expected_keymax2, 'but got', dictionary_keymax(dictionary2))
    if dictionary_keymax_count(dictionary3) != expected_keymax3:
        print('Test failed for', dictionary3, 'Expected', expected_keymax3, 'but got', dictionary_keymax(dictionary3))
    if dictionary_keymax_count(dictionary4) != expected_keymax4:
        print('Test failed for', dictionary4, 'Expected', expected_keymax4, 'but got', dictionary_keymax(dictionary4))
    print(f'Test of dictionary_keymax completed')
test_dictionary_keymax_count()



def read_file_bible(file):
    text = open("bible.txt").read()
    return text

def final_function(str):
    file_content = read_file_bible(str)
    lower_case_content = lower_case_maker(file_content)
    convert_to_list_content = convert_to_list(lower_case_content)
    string_cleaner_content= string_cleaner(lower_case_content)
    count_words_content = count_words(string_cleaner_content)
    dictionary_maker_content = dictionary_maker(string_cleaner_content)
    dictionary_count_content = dictionary_count(dictionary_maker_content)
    dictionary_value_of_keys_content = dictionary_value_of_keys(string_cleaner_content)
    dictionary_keymax_content = dictionary_keymax(dictionary_value_of_keys_content)
    dictionary_keymax_count_content = dictionary_keymax_count(dictionary_value_of_keys_content)
    return count_words_content, dictionary_count_content, dictionary_keymax_content, dictionary_keymax_count_content
def final_function_test():
    result = final_function('bible.txt')
    print('\nTest of function...')
    print('\nThe number of words in the text are:', result[0])
    print('\nThe number of different words are:', result[1])
    print('\nThe most occuring word in the text is:', result[2])
    print('\nHow many times the occuring word is repeated:', result[3])
    print('\nTest of final function completed!')
final_function_test()