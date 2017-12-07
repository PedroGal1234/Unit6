#Pedro Gallino
#12/6/17
#howManyWords.py prints how many of each word with cirtain charecters

dictionary = open('engmix.txt')
words = []
for i in range(23):
    words.append(0)

for word in dictionary:
    x = len(word.strip())
    words[x-1] +=1
    
for i in range(22):
    if words[i-1] == 1 and i != 0:
        print('There is: ',words[i-1],',',i,'letter word')
    elif words[i-1] > 1 and i != 0:
        print('There are: ',words[i-1],',',i,'letter words')



