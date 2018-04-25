#Heather Stafford
#4/23/18
#longestWord.py

words = input('Enter some words: ').split(' ')

longest = 0

for item in words:
    if len(item) > longest:
        longest = len(item)
