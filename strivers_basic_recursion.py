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
######################

#check if the string is palindome
def is_palindrome(s):
    def inner(s,l,r):
        if l>=r:
            return True
        if s[l]!=s[r]:
            return False
        return inner(s,l+1,r-1)
        
    return inner(s, 0, len(s)-1)  

#####################
#Fibonacci Series up to Nth term
def fibonacci(N):
    def inner(n):
        if n<=1:
            return n
        return inner(n-1)+inner(n-2)
    res =[]
    for i in range(0,N+1):
        res.append(inner(i))

    return res
    

def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    ans =[]
    def inner(new,idx):
        if len(new)==k and sum(new)==n:
            ans.append(new[:])
            return
        if idx ==10:
            return
        if len(new)>k:
            return
        for i in range(idx,10):
            new.append(i)
            inner(new,i+1)
            new.pop()
    inner([],1)
    return ans
    


if __name__=='__main__':
    #print_name(10,'Jesna Augustine')
    #one_n(6)
    #N_one(3)
    #print(reverse([1,2,3,4]))
    #print(is_palindrome('masam'))
    #print(fibonacci(6))
    print(combinationSum3(9, 45))
