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

if __name__=='__main__':
    print(binary_search([3, 4, 6, 7, 9, 12, 16, 17],1))