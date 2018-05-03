#Heather Stafford
#5/3/18
#gnomeSort.py

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A):
    pos = 0 
    while pos < len(A):
        if pos == 0 or A[pos] >= A[pos - 1]:
            pos = pos +1
        else:
            A[pos], A[pos - 1] = A[pos - 1], A [pos]
            pos = pos - 1
    return A
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

