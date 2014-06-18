import re
from lexicon import lexicon

alphabeta = "'? _-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#letters key length
gotton = input('letters key length:')
gotton = gotton.split(" ")

letters = gotton[0]
key = gotton[1]
length = int(gotton[2])

#initialize
word_chars = {}
gotton_chars = dict([(l, 0) for l in alphabeta])

for word in lexicon:
    word_chars[word] = dict([(l, 0) for l in alphabeta])

#count gotton chars
for char in gotton[0]:
    gotton_chars[char] += 1

#for all words
for word in lexicon:
    for char in word:
        word_chars[word][char] += 1
    for char in alphabeta:
        if gotton_chars[char] < word_chars[word][char]:
            break
        elif char == 'z' and word_chars[word][key] != 0 and len(word) == length:
            print(word)
