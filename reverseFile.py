#Pedro Gallino
#12/7/17
#reverseFile.py - reverse a list of the users choice

openFile = input('Enter a file: ')

file = open(openFile)
l = []
for line in file:
    l.append(line.strip())
l.reverse()

for i in l:
    print(i)


