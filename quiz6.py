#Pedro Gallino
#12/13/17
#quiz6.py - my unite six quiz for proggraming

"""
dictionary = open('engmix.txt')

for word in dictionary:
    cCount = 0
    pCount = 0
    
    for letter in word:
        if letter == 'c':
            cCount += 1
        elif letter == 'p':
            pCount += 1
    if cCount == 3 and pCount == 2:
        print(word.strip())
"""



dictionary = open('engmix.txt')

for word in dictionary:
    if word.strip() != '':
            if word.strip()[0] == 'r':
                print(word.strip())





"""
dictionary = open('engmix.txt')

length = int(input('Enter a number: '))

for word in dictionary:
    if len(word.strip()) == length:
        print(word.strip())
        break
    
"""


'''
dictionary = open('engmix.txt')

search = input('Enter a letter: ')
count = 0
for word in dictionary:
    if word.strip() != '':    
        if search not in word.strip():
            count += 1

print(count)

'''


"""
dictionary = open('engmix.txt')
l = []
for line in dictionary:
    if line.strip() != '':
        l.append(line.strip())

print(l[len(l[:])/2])
"""


















