#Pedro Gallino
#12/8/17
#HW.py - homework for unit 6
'''
dictionary = open('engmix.txt')

word = input('Enter a word to search for: ')
yes = False
for w in dictionary:
    if word == w.strip():
        yes = True
        break

if yes == True:
    print(word,'is in the dictionary')
else:
    print(word,'is not in the dictionary')
'''
"""
dictionary = open('engmix.txt')

neatList = []

for w in dictionary:
    neatList.append(w.strip())

num = int(input('Enter a number to search for: '))
print(neatList[num-1])
"""

'''
openFile = input('Enter a file: ')
file = open(openFile)
l = []
for line in file:
    l.append(str(line.strip())+'!')

for i in l:
    print(i)
'''
