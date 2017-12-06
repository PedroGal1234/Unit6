#Pedro Gallino
#12/6/17
#longestDictionaryWord.py - finds the longest word in the dictionary

dictionary = open('engmix.txt')

wordCount = ''
for word in dictionary:
    if len(word) > len(wordCount):
        wordCount = (word.strip())

print('Thelongest word is: ',wordCount)
