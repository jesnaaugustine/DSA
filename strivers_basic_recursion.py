#print name N time using recursion

def print_name(n,name):
    if n==0:
        return
    print(name)
    n -=1
    print_name(n,name)

##################
#print 1 to N using recursion

def one_n(N):
    def inner(n):
        if n>N:
            return
        print(n)
        inner(n+1)
    return inner(1)
###################

#print N to 1

def N_one(N):
    if N==0:
        return
    print(N)
    N_one(N-1)
###########
# som of first N numbers using recursion
def sum_n(N):
    if N ==1:
        return 1
    return N +sum_n(N-1)

###########
# factorial of n 
def factorial(N):
    if N==1:
        return 1
    if N==0:
        return 1
    return N*factorial(N-1)

# reverse an array with recursion

def reverse(arr):
    def inner(i):
        if i==0:
            return [arr[0]]
        return [arr[i]] +inner(i-1)
        
    return inner(len(arr)-1)


if __name__=='__main__':
    #print_name(10,'Jesna Augustine')
    #one_n(6)
    #N_one(3)
    print(reverse([1,2,3,4]))
