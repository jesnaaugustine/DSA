##
'''  
concept used:
1. Two pointers
2. Dutch national Flag algorithm --sort arry which have only 0,1 and 2
3. Moore’s Voting Algorithm -- get majority(more than N/2 occurance) element from array
'''

##Two Sum : Check if a pair with given sum exists in Array
#Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return 

#method 1 -using hashing:
def two_sum(arr,k):
    dict ={}
    s =0
    for i in range(len(arr)):
        rem = k-arr[i]
        if rem in dict:
            return (dict[rem],i)
        dict[arr[i]]=i
    return (-1,-1)

#method2 -using two pointers
#first sort the array and keep l point in left and r point in right, then iterate till l<r
def two_sum2(arr,k):
    s_arr = sorted(arr)
    l =0
    r = len(arr)-1
    while l<r:
        if s_arr[l]+s_arr[r]==k:
            return 'Yes'
        elif s_arr[l]+s_arr[r]<k:
            l+=1
        else:
            r-=1
    return 'No'
##########
#Sort an array of 0s, 1s and 2s
#method1 - counting 0,1,2
def count_sort(arr):
    c_1 =0
    c_0 =0
    c_2=0
    for i in arr:
        if i ==0:
            c_0+=1
        elif i==1:
            c_1 +=1
        else:
            c_2 +=1
    arr = [0]*c_0+[1]*c_1+[2]*c_2
    return arr
##method2
'''  
This problem is a variation of the popular Dutch National flag algorithm. 

This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

arr[0….low-1] contains 0. [Extreme left part]
arr[low….mid-1] contains 1.
arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
The middle part i.e. arr[mid….high] is the unsorted segment

First, we will run a loop that will continue until mid <= high.
There can be three different values of mid pointer i.e. arr[mid]
If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
Finally, our array should be sorted.
'''
def dutch_national_flag_sort(arr):
    l =0
    m =0
    h = len(arr)-1
    while m<=h:
        if arr[m]==0:
            arr[m],arr[l]=arr[l],arr[m]
            m +=1
            l+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    return arr
#############
#Find the Majority Element that occurs more than N/2 times
def majority(arr):
    dict ={}
    for i in arr:
        dict[i] = dict.get(i,0)+1
    res = [item[0] for item in dict.items() if item[1]>=len(arr)/2]
    return res
#method 2 -Moore’s Voting Algorithm
'''  
Approach: 
Initialize 2 variables:
Count –  for tracking the count of element
Element – for which element we are counting
Traverse through the given array.
If Count is 0 then store the current element of the array as Element.
If the current element and Element are the same increase the Count by 1.
If they are different decrease the Count by 1.
The integer present in Element should be the result we are expecting 
'''
def moore_voting(arr):
    c =0
    ele =float('inf')
    for i in arr:
        if c ==0:
            ele =i
            c+=1
        elif ele ==i:
            c+=1
        elif ele !=i:
            c-=1
    #checking is ele is majority or not
    cnt1 = 0
    for i in range(len(arr)):
        if arr[i] == ele:
            cnt1 += 1

    if cnt1 > (len(arr) / 2):
        return ele
    return -1

 #######
 # #Maximum Subarray Sum in an Array -kaden's algorithm
def max_sum(arr):
    max_s = float('-inf')
    c_s =0
    for i in range(len(arr)):
        c_s +=arr[i]
        max_s = max(max_s,c_s)
        if c_s<0:
            c_s =0
        
    return max_s
        
    
           
if __name__=='__main__':
    #print(two_sum2([2,6,5,8,11],14))
    #print(count_sort([0,2,2,1,0,1,1]))
    #print(dutch_national_flag_sort([1,2,0,0,2,1,1]))
    #print(moore_voting([1,2]))
    print(max_sum([1,-3,4,-1,2,1,-5,4]))
    #print(max_sum([1,2,3]))