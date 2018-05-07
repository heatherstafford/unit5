#Heather Stafford
#5/7/18
#quiz5.py

def penultimate(L):
    L[int(len(L)) - 1]
    
print(penultimate([3,4,5,6,7]))


def plusEquals(A, B):
    new = []
    for item in A:
        new.append(item + B) 
    return new
    
smallest = 0
def smallest(C):
    for item in C:
        if item > smallest:
            smallest = smallest + item
    

print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))