import random as rd


def make_anagramm(word):
    word_list = list(word)
    rd.shuffle(word_list)
    return ''.join(word_list)


word = input()

print(make_anagramm(word))
