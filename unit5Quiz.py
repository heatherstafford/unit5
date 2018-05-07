#Heather Stafford
#5/7/18
#quiz5.py

def penultimate(L):
    L[len(L) - 1]
    
print(penultimate([3,4,5,6,7]))


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
    
def decimalRange(D):
    F = []
    for i in range(float(D[0]), float(D[1]), float(D[2])):
        print(i)

print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
print(decimalRange([4,10,0.5]))