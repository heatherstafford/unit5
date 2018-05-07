#Heather Stafford
#5/7/18
#quiz5.py

def penultimate(L):
    print(L[len(L)-2])

def plusEquals(A, B):
    new = []
    for item in A:
        new.append(item + B) 
    return new

def smallest(C):
    small = 100
    for item in C:
        if item < small:
            small = item
    return small

penultimate([3,4,5,6,7])
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
