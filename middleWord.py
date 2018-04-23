#Heather Stafford
#4/23/18
#middleword.py

words = input('Enter some words: ').split(' ')

num = int(len(words)%2)

if num == 0:
    print(words[len(words)/2])
    print(words[len(words)/2 +1])
elif num != 0:
    print(words[len(words)/2])