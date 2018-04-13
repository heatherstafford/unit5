#Heather Stafford
#4/13/18
#lsitDemo.py - print out first and last work in a list

words = input('Enter some words: ').split(' ')

print(words)

print('The first word was: ', words[0])
print('The last word was: ', words[-1])

#print out the list one item at a time
for item in words: 
    print(item)