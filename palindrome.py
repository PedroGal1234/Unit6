#Pedro Gallino
#12/7/17
#palindrome.py - checks for the palindromes

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    x = list(word)
    x.reverse()
    if x == list(word):
        print(word)
    

