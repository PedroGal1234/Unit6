#Pedro Gallino
#12/6/17
#zzwords.py - prints out all the words that contain 'zz'

dictionary = open('engmix.txt')

wordCount = 0

for word in dictionary:
    if 'zz' in word:
        print(word.strip())
    wordCount += 1

