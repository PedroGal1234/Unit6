#Pedro Gallino
#12/11/17
#warmUp16.py - my 16th warm up

dictionary = open('engmix.txt')
first = input('Enter your first name: ')
last = input('Enter you last name: ')

for word in dictionary:
    if word.strip() != '':
        if word.strip()[0] == first[0] and word.strip()[-1] == last[0]:
            print(word.strip())

