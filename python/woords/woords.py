import re
from lexicon import lexicon

alphabeta = "'? _-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#letters key length
gotton = input('letters key length:')
gotton = gotton.split(" ")

letters = gotton[0]


#initialize
word_chars = {}
gotton_chars = {}

#count gotton chars
for char in gotton[0]:
    gotton_chars[char] = gotton_chars.get(char, 0) + 1

#for all words
for word in lexicon:
    word_chars[word] = {}
    for char in word:
        word_chars[word][char] = word_chars[word].get(char, 0) + 1
    for char in word:
        if gotton_chars.get(char, 0) < word_chars[word].get(char, 0):
            break
        elif char == word[-1]:
            print(word)
input('end')