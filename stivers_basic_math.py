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


if __name__=='__main__':
    #print(count_digits_2(1000))
    #print(reverse(10002))
    print(is_palindrome_2(1001))
