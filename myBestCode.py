# получаем список из инпутов
def get_inputs_list(length):
    list_of_inputs = []

    for word in range(length):
        list_of_inputs.append(input())

    return list_of_inputs


# получаем словарь из списка list_of_inputs
def get_dictionary_from_inputs(list_of_terms):
    prog_dict = {}
    lenght_of_inputs = len(list_of_terms)

    for iteration in range(lenght_of_inputs):
        for_dict = list_of_terms[iteration].split(':')
        trim_dict_space = for_dict[1].lstrip()
        capitalized_keys = for_dict[0].capitalize()
        prog_dict.setdefault(capitalized_keys, trim_dict_space)

    return prog_dict


# получаем значения из prog_dict и выводим их
def get_description_from_dict(count_of_requests, programmer_dictionary):
    descriptions_list = []
    for request in range(count_of_requests):
        ask_for_word = input()
        capitalized_first_letter = ask_for_word.capitalize()
        get_value_from_dict = programmer_dictionary.get(capitalized_first_letter, 'Не найдено')
        descriptions_list.append(get_value_from_dict)

    return descriptions_list

# печатаем с новой строки описания слов
def unpacked_descriptions_of_terms(list_descriptions_of_terms):
    for description in list_descriptions_of_terms:
        print(description)


# считывааем количество инпутов словаря
count_of_dict_strings = int(input())
list_of_inputs = get_inputs_list(count_of_dict_strings)
programmer_dict = get_dictionary_from_inputs(list_of_inputs)


# считываем количество запросов слов из словаря
count_of_requests = int(input())
descriptions_of_terms = get_description_from_dict(count_of_requests, programmer_dict)
unpacked_descriptions_of_terms(descriptions_of_terms)
