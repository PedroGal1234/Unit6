#Pedro Gallino
#12/11/17
#warmup16.py - how to read a file

dictionary = open('engmix.txt')
first = input('Enter your first name: ')
last = input('Enter your last name: ')
for word in dictionary:
    if word.strip() != '':
        if word.strip()[0] == first[0] and word.strip()[-1] == last[0]:
            print(word.strip())