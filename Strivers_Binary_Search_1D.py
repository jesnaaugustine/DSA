#########
#Binary serach for target K in array
'''  
Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.

'''
def binary_search(arr,k):
    l =0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==k:
            return 'Yes'
        elif arr[mid]<k:
            l=mid+1
        else:
            r =mid-1
    return 'No'
#######
#Implement Lower Bound
'''  
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] >= x.
'''

def lower_bound(arr,k):
    l =0
    r = len(arr)-1
    ans =len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==k:
            while arr[mid]==k:
                mid-=1
            return mid+1
        elif arr[mid]<k:
            l=mid+1
        else:
            ans = min(ans,mid)
            r=mid-1
    return ans
#######
#Implement Upper Bound
''' 
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.

Example 2:
Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
Result: 4
Explanation: Index 4 is the smallest index such that arr[4] > x.

'''

def upper_bound(arr,k):
    l =0
    r = len(arr)-1
    ans = len(arr)
    while l<=r:
        m = (l+r)//2
        if arr[m]<=k:
            l+=1
        else:
            ans = min(ans,m)
            r-=1
    return ans
########
#Search Insert Position
'''  
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.
xample 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.

'''
def insert_index(arr,k):
    l =0
    r = len(arr)-1
    ans = len(arr)
    while l<=r:
        m = (l+r)//2
        if arr[m]==k:
            return m
        elif arr[m]<k:
            l=m+1
        else:
            ans=min(m,ans)
            r=m-1
    return ans

#########
#Floor and Ceil in Sorted Array
'''  
Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.
Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Example 2:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
Result: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.


'''
def floor_ceil(arr,k):
    f = 0
    c =len(arr)-1
    l =0
    r = len(arr)-1
    while l<=r:
        m =(l+r)//2
        if arr[m]<k:
            f = max(f,m)
            l=m+1
        elif arr[m]>k:
            c = min(c,m)
            r =m-1
        else:
            f = m
            c =m
            return arr[f],arr[c]
    return arr[f],arr[c]
##########
#Last occurrence in a sorted array
''' 
Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

'''
def last_occ(arr,k):
    ans = -1
    s =0
    l =len(arr)-1
    while s<=l:
        m =(s+l)//2
        if arr[m]==k:
            ans = max(ans,m)
            s=m+1
        elif arr[m]<k:
            s =m+1
        else:
            l = m-1
    return ans

#######
#Count Occurrences in Sorted Array
''' 
Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.
Example 1:
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.

'''
def count_occ(arr,k):
    count =0
    s =0
    l = len(arr)-1
    while s<=l:
        m =(s+l)//2
        if arr[m]==k:
            while m>=0 and arr[m]==k:
                m-=1
                count+=1
            m =m+count
            while m<len(arr) and arr[m]==k :
                m+=1
                count+=1
            return count-1
        elif arr[m]<k:
            s =m+1
        else:
            l =m-1
    return count
######
#Search Element in a Rotated Sorted Array
'''  
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1

'''
def search_rotated(arr,k):
    l =0
    r = len(arr)-1
    while l<=r:
        m =(l+r)//2
        if arr[m]==k:
            return m
        elif m!=0 and m!=len(arr)-1 and arr[m]>arr[m-1] and arr[m]>arr[m+1]:
            if arr[l]<=k<=arr[m-1]:
                r = m-1
            else:
                l =m+1
        elif arr[m]>k:
            r =m-1
        elif arr[m]<k:
            l=m+1
    return -1
##########
#Search Element in Rotated Sorted Array II
'''  
Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 
Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.


'''
def bs_rotated(arr,k):
    l =0
    r = len(arr)-1
    while l<=r:
        m =(l+r)//2
        if arr[m]==k:
            return True
        elif arr[l]<=arr[m]:
            if arr[l]<=k and k<=arr[m]:
                r =m-1
            else:
                l = m+1
        else:
            if arr[m]<=k and k<=arr[r]:
                l=m+1
            else:
                r =m-1
    return False
########
#Minimum in Rotated Sorted Array

'''  
Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 0
Explanation: Here, the element 0 is the minimum element in the array.

'''
def min_rotated(arr):
    l =0
    r =len(arr)-1
    g_min =float('inf')
    while l<=r:
        m = (l+r)//2
        if arr[l]<=arr[m]:
            g_min = min(arr[l],g_min)
            l =m+1
        else:
            g_min = min(g_min,arr[m])
            r=m-1
    return g_min
#######
#Find out how many times the array has been rotat
'''  
Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.


'''
def rotation_count(arr):
    l =0
    r =len(arr)-1
    g_min = float('inf')
    g_count = 0
    while l<=r:
        m =(l+r)//2
        if arr[l]<=arr[m]:
            if arr[l]<g_min:
                g_min = arr[l]
                g_count =max(g_count,l)
            l =m+1
        else:
            if arr[m]<g_min:
                g_min = arr[m]
                g_count = max(g_count,m)
            r=m-1
    return g_count
#######
#Search Single Element in a sorted array
'''  
Input Format: arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result: 4
Explanation: Only the number 4 appears once in the array.

'''

def single_ele(arr):
    l =0
    r =len(arr)-1
    while l<=r:
        m =(l+r)//2
        if arr[m]!=arr[m-1] and arr[m]!=arr[m+1]:
            return arr[m]
        elif (m%2==0 and arr[m+1]==arr[m]) or (m%2==1 and arr[m]==arr[m-1]):
            l = m+1
        else:
            r = m-1
    return -1

#########
#Finding Sqrt of a number using Binary Search
'''  
Problem Statement: You are given a positive integer n. Your task is to find and return its square root. 
If ‘n’ is not a perfect square, then return the floor value of 'sqrt(n)'.

'''
def sqrt(n):
    l =0
    r =n
    ans =0
    while l<=r:
        m =(l+r)//2
        if m*m <=n:
            ans = max(ans,m)
            l=m+1

        else:
            r =m-1
    return ans

###########
#Koko Eating Bananas
'''  
roblem Statement: A monkey is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.

Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas. If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

Example 1:
Input Format: N = 4, a[] = {7, 15, 6, 3}, h = 8
Result: 5
Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

Example 2:
Input Format: N = 5, a[] = {25, 12, 8, 14, 19}, h = 5
Result: 25
Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.

'''
#brute force
import math
def koko_eating(arr,h):
    if len(arr)>h:
        return -1
    #min bananas eating =1 and max can be max(arr)
    ans = max(arr)
    for i in range(1,max(arr)+1):
        cur =0
        for a in arr:
            cur+=math.ceil(a/i)
        if cur <=h:
            return i
    return -1

#using binary search: search range is from 1 to max(arr). If hour to each for mid no of bananas eating hour less than h r=mid -1
#else l = mod +1
def hourtaken(arr,k):
    cur =0
    for a in arr:
        cur+=math.ceil(a/k)
    return cur
def kok_eating_bs(arr,h):
    ans =max(arr)
    if len(arr)>h:
        return -1
    l =1
    r = max(arr)
    while l<=r:
        mid =(l+r)//2
        localh = hourtaken(arr,mid)
        if localh<=h:
            ans = min(ans,mid)
            r = mid-1
        else:
            l = mid+1
    return ans
def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    ans =max(piles)
    if len(piles)>h:
        return -1
    l =1
    r = max(piles)
    while l<=r:
        mid =(l+r)//2
        cur =0
        for a in piles:
            cur+=math.ceil(a/mid)
        localh =cur
        if localh<=h:
            ans = min(ans,mid)
            r = mid-1
        else:
            l = mid+1
    return ans
##########
#Minimum days to make M bouquets
'''  
Problem Statement: You are given 'N’ roses and you are also given an array 'arr'  where 'arr[i]'  denotes that the 'ith' rose will bloom on the 'arr[i]th' day.
You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses. Return -1 if it is not possible.

Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

'''
def check_required(arr,k):
    cur_s =0
    total =0
    for i in arr:
        if i ==1:
            cur_s+=1
        else:
            total +=cur_s//k
            cur_s =0
    total +=cur_s//k
    return total
def bouquet_make(arr,m,k):
    l = min(arr)
    r = max(arr)
    if m*k>len(arr):
        return -1
    while l<=r:
        mid = (l+r)//2
        new_arr =[]
        for i in range(len(arr)):
            if arr[i]<=mid:
                new_arr.append(1)
            else:
                new_arr.append(0)
        total = check_required(new_arr,k)
        if total <m:
            l =mid+1
        elif total>m:
            r =mid-1
        else:
            return mid
    return -1




if __name__=='__main__':
    #print(binary_search([3, 4, 6, 7, 9, 12, 16, 17],1))
    #print(lower_bound([1,2,2,3],2))
    #print(upper_bound([1,2,2,3],2))
    #print(insert_index([1,2,4,7],0))
    #print(floor_ceil([3, 4, 4, 7, 8, 10],8))
    #print(last_occ([3,4,13,13,13,20,40],40))
    #print(count_occ([2, 2 , 3 , 3 , 3 , 3 , 4],2))
    #print(search_rotated([4,5,6,7,0,1,2,3],4))
    #print(bs_rotated([7, 8, 1, 3, 3, 3, 4, 5, 6],2))
    #print(min_rotated([4,5,6,7,0,1,2,3,3]))
    #print(rotation_count([3,4,5,6,7,0,1,2,3]))

    #print(single_ele([1,2,2,3,3,4,4,5,5,6,6]))
    #print(sqrt(36))
    #print(minEatingSpeed([30,11,23,4,20],6))
    print(bouquet_make([1, 10, 3, 10, 2],2,3))