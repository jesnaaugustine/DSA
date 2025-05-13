##
'''  
concept used:
1. Two pointers
2. Dutch national Flag algorithm --sort arry which have only 0,1 and 2
3. Moore’s Voting Algorithm -- get majority(more than N/2 occurance) element from array
4. Kadane's Algorithm - maximum sum subarray
5. transpose a matrix
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
''' 
We will run a loop(say i) to iterate the given array.
Now, while iterating we will add the elements to the sum variable and consider the maximum one.
If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.
  '''
def max_sum(arr):
    max_s = float('-inf')
    c_s =0
    for i in range(len(arr)):
        c_s +=arr[i]
        max_s = max(max_s,c_s)
        if c_s<0:
            c_s =0
        
    return max_s
##########
#Maximum Subarray Sum in an Array - returs array
import copy
def subarray_max_sum(arr):
    max_s =float('-inf')
    #dummy_ar =[]
    #arr_r =[]
    c_s =0
    l =0
    r =0
    s =0
    for i in range(len(arr)):
        c_s +=arr[i]
        #dummy_ar.append(arr[i])
        if c_s>max_s:
            max_s =c_s
            #arr_r =copy.copy(dummy_ar)
            l =s
            r =i
        if c_s<0:
            c_s=0
            s =i+1
            #dummy_ar =[]
    return arr[l:r+1],max_s

######
#Stock Buy And Sell--two pinters
def stock(arr):
    b =0
    s =0
    profit = 0
    while s<len(arr):
        profit =max(profit, arr[s]-arr[b])
        if arr[s]<arr[b]:
            b = s
        s+=1
    return profit

######
#Rearrange Array Elements by Sign
''' 
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
'''
#method 1 - brute force -time complexity -N^2
def alternative_sign(arr):
    arr_pos =[]
    arr_neg =[]
    for a in arr:
        if a>=0:
            arr_pos.append(a)
        else:
            arr_neg.append(a)
    l =0
    ans =[]
    while l<len(arr_pos) and l<len(arr_neg):
        ans.append(arr_pos[l])
        ans.append(arr_neg[l])
        l+=1
    if l!=len(arr_pos):
        ans.extend(arr_pos[l:])
    if l!=len(arr_neg):
        ans.extend(arr_neg[l:])
    return ans

    
#method 2 - not in place - create new array
def alternative_sign2(arr):
    ans =[0]*len(arr)
    pos_i =0
    neg_i =1
    for a in arr:
        if a>=0:
            ans[pos_i]=a
            pos_i +=2
        else:
            ans[neg_i]=a
            neg_i+=2
    return ans
##########
# #next_permutation : find next lexicographically greater permutation
''' 
1.Find the break-point, i: Break-point means the first index i from the back of the given array where arr[i] becomes smaller than arr[i+1].
    For example, if the given array is {2,1,5,4,3,0,0}, the break-point will be index 1(0-based indexing). Here from the back of the array, index 1 is the first index where arr[1] i.e. 1 is smaller than arr[i+1] i.e. 5.
    To find the break-point, using a loop we will traverse the array backward and store the index i where arr[i] is less than the value at index (i+1) i.e. arr[i+1].
2. If such a break-point does not exist i.e. if the array is sorted in decreasing order, the given permutation is the last one in the sorted order of all possible permutations. So, the next permutation must be the first i.e. the permutation in increasing order.
    So, in this case, we will reverse the whole array and will return it as our answer.
3.If a break-point exists:
    3.1. Find the smallest number i.e. > arr[i] and in the right half of index i(i.e. from index i+1 to n-1) and swap it with arr[i].
    3.2.1 Reverse the entire right half(i.e. from index i+1 to n-1) of index i. And finally, return the array.
'''
def next_per(arr):
    break_in = -1
    for i in range(len(arr)-1,0,-1):
        if arr[i]>arr[i-1]:
            break_in = i-1
            break
    if break_in ==-1:
        ans  =arr[len(arr)-1::-1]
        return ans
    for j in range(len(arr)-1,break_in,-1):
        if arr[break_in]<arr[j]:
            arr[break_in],arr[j]=arr[j],arr[break_in]
            break

    ans = arr[:break_in+1]+arr[len(arr)-1:break_in:-1]
    return ans
#######
#Leaders in an Array
''' 
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
'''
def leaders(arr):
    res =[]
    g_max = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>g_max:
            res.append(arr[i])
        g_max =max(g_max,arr[i])
    return res
############
#Longest Consecutive Sequence in an Array
''' 
Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

Input: [3, 8, 5, 7, 6]

Output: 4

Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.
'''
def con_seq(arr):
    s_arr=sorted(arr)
    l =0
    s=0
    e =1
    c_l =1
    while e<len(arr):
        if s_arr[e]-s_arr[s] !=c_l:
            s=e
            c_l =1
            
        else:
            c_l+=1
            l = max(l,e-s+1)
        e+=1
    return l
##########
#Set Matrix Zero
'''  
Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
'''
def set_matrix(arr):
    zero =[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                zero.append((i,j))
    for k in zero:
        arr[k[0]] = [0]*len(arr[0])
        for l in range(len(arr)):
            arr[l][k[1]]=0
    return arr

#########
#Rotate Image by 90 degree
''' 
Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: [[7,4,1],[8,5,2],[9,6,3]]

'''

def rotate_90(arr):
    n = len(arr)
    rotated = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(n):
        for j in range(len(arr[0])):
            rotated[j][n - i - 1] = arr[i][j]
    return rotated
##transpose the matrix and reverese each row 
def rotate_90_2(arr):
    r = len(arr)
    c = len(arr[0])
    for i in range(r):
        for j in range(i):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    for i in range(r):
        arr[i] = arr[i][c-1::-1]
    return arr
if __name__=='__main__':
    #print(two_sum2([2,6,5,8,11],14))
    #print(count_sort([0,2,2,1,0,1,1]))
    #print(dutch_national_flag_sort([1,2,0,0,2,1,1]))
    #print(moore_voting([1,2]))s
    #print(subarray_max_sum([1,-3,4,-1,2,1,-5,4]))
    #print(max_sum([1,2,3]))
    #print(stock([7,1,5,3,6,4]))
    #print(alternative_sign([1,2,3,-1,-2,-3,-3,5,6,7,8]))
    #print(next_per([5,4,3,2,1]))
    #print(leaders([10, 22, 12, 3, 0, 6]))
    #print(con_seq([3, 8, 5, 7, 6]))
    #print(set_matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    print(rotate_90_2([[1,2,3],[4,5,6],[7,8,9]]))