#Implement Pow(x,n) | X raised to the power N
'''  
if n <0, then take ans(n) and ans =1/x^n
if n is too high then ans will exceed, to avoid this follow below steps:
    If the exponent is even, we square the base as xn = (x2)n/2.
    If the exponent is odd, the algorithm multiples the result by the base as xn = x(xn-1).
'''
def power(x,n):
    def inner(x,n):
        if n==0:
            return 1
        if n%2==0:
            return inner(x*x,n//2)
        else:
            return x*inner(x,n-1)
        
    p = inner(x,abs(n))
    if n<0:
        return 1/p
    else:
        return p

############
#1922. Count Good Numbers
'''  
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
'''
def countGoodNumbers(n):
    def inner_pow(x,n):
            x%=mod
            if n==0:
                return 1
            if n%2==0:
                return inner_pow(x*x,n//2)%mod
            else:
                return x*inner_pow(x,n-1)%mod

    t_even = 5
    t_odd =4
    mod = 10**9 + 7
    if n%2==0:
        odd = n//2
        even = n//2
    else:
        odd = n//2
        even = n//2+1
    return (inner_pow(t_even,even)*inner_pow(t_odd,odd))%mod
    
        
if __name__=='__main__':
    #print(power(2,10))
    print(countGoodNumbers(50))