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

if __name__=='__main__':
    #print(binary_search([3, 4, 6, 7, 9, 12, 16, 17],1))
    print(lower_bound([1,2,2,3],2))