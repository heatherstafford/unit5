#Heather Stafford
#4/25/18
#dictionaryDemo.py - most list practice

words = ['computer','mortify','dog','firetruck','yes','python','cat']

words.sort()

num = int(input('What number word do you want? '))
if num<= 0 or num >= len(words)+1:
    print('Invalid number')
else:
    print(words[num - 1])
