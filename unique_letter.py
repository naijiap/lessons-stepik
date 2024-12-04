def check_unique_letters(word):
    new_word = word.lower()
    my_set = set()
    for letter in new_word:
        my_set.add(letter)
    amount_of_unique = len(my_set)
    return amount_of_unique


word_count = int(input())
for _ in range(word_count):
    word = input()
    print(check_unique_letters(word))