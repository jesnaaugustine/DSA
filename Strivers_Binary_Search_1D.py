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




if __name__=='__main__':
    #print(binary_search([3, 4, 6, 7, 9, 12, 16, 17],1))
    #print(lower_bound([1,2,2,3],2))
    #print(upper_bound([1,2,2,3],2))
    #print(insert_index([1,2,4,7],0))
    #print(floor_ceil([3, 4, 4, 7, 8, 10],8))
    #print(last_occ([3,4,13,13,13,20,40],40))
    #print(count_occ([2, 2 , 3 , 3 , 3 , 3 , 4],2))
    #print(search_rotated([4,5,6,7,0,1,2,3],4))
    print(bs_rotated([7, 8, 1, 3, 3, 3, 4, 5, 6],2))