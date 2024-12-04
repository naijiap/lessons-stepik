import random as rd


def make_anagramm(word):
    word_list = list(word)
    rd.shuffle(word_list)
    return ''.join(word_list)


Word = input()

print(make_anagramm(Word))
