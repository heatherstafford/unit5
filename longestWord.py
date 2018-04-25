#Heather Stafford
#4/23/18
#longestWord.py

words = input('Enter some words: ').split(' ')

longest = 0
word = ' '

for item in words:
    if len(item) > longest:
        longest = len(item)
        word = item
print('The longest word is', word)
