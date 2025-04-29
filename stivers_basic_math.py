#######count digits

#method1- convert to string and take len

def count_digits(N):
    return len(str(N))

#method2


def count_digits_2(N):
    result =0
    while N>0:
        N=N//10
        result +=1
    return result
#method3 - take log 10 of number +1
#########################################

######Reverse digits of number
#method1
def reverse(N):
    result =0
    while N>0:
        result = result *10 +N%10
        N=N//10
    return result
        
 #######################################
# number is palindrome or not
#method 1
def is_palindrome(N):
    return str(N)==str(N)[-1::-1]


#method2
def is_palindrome_2(N):
    n_s = str(N)
    result = True
    for i in range(len(n_s)//2):
        if n_s[i] != n_s[len(n_s)-1-i]:
            return False
    return result
#######
#GCD of two numbers
#get prime factors of number then get 
from prime_calculator import Prime
from functools import reduce
def gcd(N1,N2):
    prime1= Prime(N1)
    factors1 = prime1.prime_factors()
    prime2 = Prime(N2)
    factors2 = prime2.prime_factors()
    fact_set1 = set(factors1.keys())
    fact_set2 = set(factors2)
    c_set = fact_set1.intersection(fact_set2)
    if len(c_set)==0:
        return 1
    result = reduce(lambda x,y: (x**(min(factors1[x],factors2[x])))*(y**(min(factors1[y],factors2[y]))),c_set)
    return result

#method2 - gcd of two numbers equals to gcd of min number subr=trascted from other
''' 
Eg, n1 = 20, n2 = 15:

gcd(20, 15) = gcd(20-15, 15) = gcd(5, 15)

gcd(5, 15) = gcd(15-5, 5) = gcd(10, 5)

gcd(10, 5) = gcd(10-5, 5) = gcd(5, 5)

gcd(5, 5) = gcd(5-5, 5) = gcd(0, 5)

Hence, return 5 as the gcd.
'''
def gcd_2(N1,N2):
    if N1 ==0 or N2 ==0:
        return max(N1,N2)
    return gcd_2(min(N1,N2),max(N1,N2)-min(N1,N2))
    


if __name__=='__main__':
    #print(count_digits_2(1000))
    #print(reverse(10002))
    #print(is_palindrome_2(1001))
    print(gcd_2(20,10))
