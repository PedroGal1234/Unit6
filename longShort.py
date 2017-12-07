#Pedro Gallino
#12/6/17
#longestDictionaryWord.py - finds the longest word in the dictionary

dictionary = open('engmix.txt')
longest = ['']*26
alphe = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def long(j):
    wordCount = ''
    for word in j:
        if len(word) > len(wordCount):
            wordCount = (word.strip())
    return wordCount

def short(l):
    wordCount1 = ''
    for word in j:
        if len(word) < len(wordCount):
            wordCount1 = (word.strip())
    return wordCount1

for word in dictionary:
    alphabet(word[0])

