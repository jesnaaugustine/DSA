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
##########
#sum of first N numbers
def sum_n(N):
    if N ==0:
        return 0
    return N+sum_n(N-1)

#reverse an array
def reverse(arr):
    new =[]
    def inner(new,arr,n):
        if n<0:
            return new
        new.append(arr[n])
        return inner(new,arr,n-1)
    return inner(new,arr,len(arr)-1)
#inplace
def reverse_inplace(arr):
    def inner(l,r):
        if l>r:
            return arr
        arr[l],arr[r]=arr[r],arr[l]
        return inner(l+1,r-1)
    return inner(0,len(arr)-1)
##########
#print all subsequence
def sub_seq(arr):
    ans =[]
    def inner(ind,new):
        if ind ==len(arr):
            ans.append(new.copy())
            return
        new.append(arr[ind])
        inner(ind+1,new)
        new.pop()
        inner(ind+1,new)
    inner(0,[])
    return ans
###########
#subsequence whose sum is K
def sub_sum_k(arr,K):
    ans =[]
    def inner(ind,new):
        if ind == len(arr):
            if sum(new)==K:
                ans.append(new.copy())
                return True
            else:
                return False
            
        new.append(arr[ind])
        flag1 =inner(ind+1,new)
        if flag1:
            return True
        new.pop()
        flag2 =inner(ind+1,new)
        if flag2:
            return True
        return False
    inner(0,[])
    return ans
#######
#39. Combination Sum
''' 
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
 '''
def combination_sum(arr,target):
    ans = []
    def inner(ind,new,s):
        if s==target:
            ans.append(new.copy())
            return
        elif s>target:
            return
        if ind ==len(arr):
            return 
        new.append(arr[ind])
        s +=arr[ind]
        inner(ind,new,s)
        new.pop()
        s-=arr[ind]
        inner(ind+1,new,s)
    inner(0,[],0)
    return ans


#######
#Combination Sum II
'''  
Given a collection of candidate numbers (candidates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def inner(ind,s,new):
            if s ==target:
                if new[:] not in ans:
                    ans.append(new[:])
                return 
            if ind ==len(candidates):
                return
            if s>target:
                return
            new.append(candidates[ind])
            s+=candidates[ind]
            inner(ind+1,s,new)
        inner(0,0,[])
        return ans
#####optimized
def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def inner(ind,s,new):
            if s ==target:
                if new[:] not in ans:
                    ans.append(new[:])
                return 
            if ind ==len(candidates):
                return
            if s>target:
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                new.append(candidates[i])
                s+=candidates[i]
                inner(i+1,s,new)
                new.pop()
                s-=candidates[i]
            
        inner(0,0,[])
        return ans

######
#ubset Sum : Sum of all Subsets
''' 
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples:

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8
'''

def subset_sum(arr):
    res = []
    arr.sort(reverse=True)
    def inner(ind,s):
        if ind==len(arr):
            res.append(s)
            return
        s+=arr[ind]
        inner(ind+1,s)
        s-=arr[ind]
        inner(ind+1,s)
    inner(0,0)
    return res
#####################
#generate all combination for [1,n]
def combination(n):
    res =[]
    def inner(ind,new):
        #res.append(new[:])
        if ind == n+1:
            res.append(new[:])
            return
        for i in range(ind,n+1):
            new.append(i)
            inner(i+1,new)
            new.pop()
    inner(1,[])
    return res

#generate all combination with k length for above problem
def combination_k(n,k):
    res =[]
    def inner(ind,new):
        if len(new)==k:
            res.append(new[:])
            return
        
        for i in range(ind,n+1):
            new.append(i)
            inner(i+1,new)
            new.pop()
    inner(1,[])
    return res
#generate all combinations with sum =target for above problem
def combination_sum_n(n,target):
    res =[]
    def inner(ind,new,s):
        if s==target:
            res.append(new[:])
            return
        if ind >=n+1 or s>target:
            return
        for i in range(ind,n+1):
            new.append(i)
            s+=i
            inner(i+1,new,s)
            s-=i
            new.pop()
    inner(1,[],0)
    return res

if __name__=='__main__':
    #print(power(2,10))
    #print(countGoodNumbers(50))
    #print(sum_n(3))
    #print(reverse_inplace([1,2,3,4,5]))
    #print(sub_seq([1,2]))
    #print(sub_sum_k([1,2,1],2))
    #print(combination_sum([2,3,6,7],7))
    #print(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],3))
    #print(subset_sum([5,2,1]))
    print(combination(2))
    #print(combination_sum_n(4,5))