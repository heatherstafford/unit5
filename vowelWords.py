#Heather Stafford
#4/26/18
#vowelWordsDemo.py

words = input('Enter some words: ').split(' ')

for item in words:
    if item[0] in 'AEIOUaeiou':#starts with vowel
        print(item)
