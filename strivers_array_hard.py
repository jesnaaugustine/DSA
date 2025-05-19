###########
#Program to generate Pascal's Triangle
''' 
Poblem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:


Example 1:
Input Format: N = 5, r = 5, c = 3
Result: 6 (for variation 1)
1 4 6 4 1 (for variation 2)

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1    (for variation 3)

'''

def pascals(N):
    DP =[]
    if N==1:
        DP.append([1])
        return DP
    DP=[[1],[1,1]]
    for i in range(2,N):
        temp =[]
        temp.append(1)
        for j in range(len(DP[-1])-1):
            temp.append(DP[-1][j]+DP[-1][j+1])
        temp.append(1)
        DP.append(temp)
    return DP
##########
#Majority Elements(&gt;N/3 times) | Find the elements that appears more than N/3 times in the array
''' 
Example 1:
Input Format: N = 5, array[] = {1,2,2,3,2}
Result: 2
Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.
max no of element with count n/3 is 2
'''
def majority_3(arr):
    dict ={}
    res =[]
    for i in arr:
        dict[i] = dict.get(i,0)+1
        if dict[i]==int(len(arr)/3+1):
            res.append(i)
        if len(res)==2:
            break
    return res

    #res = [item[0] for item in dict.items() if item[1]>=len(arr)/3]
    #return res

##extended version of muloors voting algorithm
def majority_3_2(arr):
    cnt1 =0
    cnt2 =0
    ele1 =0
    ele2 =0
    for i in arr:
        if cnt1==0 and ele2!=i:
            cnt1 =1
            ele1 =i
        elif cnt2==0 and ele1!=i:
            cnt2=1
            ele2=i
        elif i==ele1:
            cnt1+=1
        elif i==ele2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2 -=1
    res =[]
    e1=0
    e2=0
    for i in arr:
        if i==ele1:
            e1+=1
        elif i==ele2:
            e2+=1
    if e1>=int(len(arr)/3+1):
        res.append(ele1)
    if e2>=int(len(arr)/3+1):
        res.append(ele2)
    return res
#######
# 3 Sum : Find triplets that add up to a zero
'''  
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k
'''
#hashing
def sum_3(arr):
    res =set()
    for i in range(len(arr)):
        temp =set()
        for j in range(i+1,len(arr)):
            if 0-arr[i]-arr[j] in temp:
                x=sorted([arr[i],arr[j],(0-arr[i]-arr[j])])
                res.add(tuple(x))
            temp.add(arr[j])
    result = list(res)
    return result
#method 2 - two pointers
def sum_3_two(arr):
    s_arr =sorted(arr)
    res =set()
    for i in range(len(s_arr)):
        l = i+1
        r = len(arr)-1
        while l<r:
            if s_arr[i]+s_arr[l]+s_arr[r]==0:
                x = [s_arr[i],s_arr[l],s_arr[r]]
                res.add(tuple(x))
                l+=1
                r-=1
            elif s_arr[i]+s_arr[l]+s_arr[r]<0:
                l+=1
            else:
                r-=1
    return list(res)
            
##########
#4 sum
''' 
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

'''
def sum_4(arr,k):
    arr = sorted(arr)
    res = set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            l =j+1
            r = len(arr)-1
            while l<r:
                rem = k-arr[i]-arr[j]
                if arr[l]+arr[r]==rem:
                    res.add(tuple([arr[i],arr[j],arr[l],arr[r]]))
                    l+=1
                    r-=1
                elif arr[l]+arr[r]<rem:
                    l+=1
                else:
                    r-=1
    return list(res)
                
########
#Length of the longest subarray with zero Sum
'''  
Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result: 5
Explanation: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5!

'''
def lon_sub(arr):
    max_l = 0
    cur_sum =0
    dict ={}
    for i in range(len(arr)):
        cur_sum+=arr[i]
        if cur_sum==0:
            max_l= max(max_l,i+1)
        rem = cur_sum-0
        if rem in dict:
            max_l=max(max_l,i-dict[cur_sum])
        dict[cur_sum] = min(dict.get(cur_sum,i),i)
    return max_l

#######
#Count the number of subarrays with given xor K

''' 
Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
'''
def xor_sub(arr,k):
    cur =0
    dict={}
    max_c =0
    for i in range(len(arr)):
        cur = cur^arr[i]
        if cur==k:
            max_c+=1
        rem = cur^k
        if rem in dict:
            max_c+=dict[rem]
        dict[cur]=dict.get(cur,0)+1
    return max_c

##########
#Merge Overlapping Sub-intervals
''' 
Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.
Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
 intervals.
'''
def merge_int(arr):
    arr =sorted(arr,key = lambda x:x[0])
    l = arr[0][0]
    r =arr[0][1]
    res =[]
    for i in range(1,len(arr)):
        if arr[i][0]<=r:
            r=max(r,arr[i][1])
        else:
            res.append([l,r])
            l=arr[i][0]
            r =arr[i][1]
    res.append([l,r])
    return res
#######
#Merge two Sorted Arrays Without Extra Space
''' 
Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
Example 1:

Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]

Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]

'''
#with extra array
def merge_array(arr1,arr2):
    res =[]
    l =0
    r =0
    while l<len(arr1) and r<len(arr2):
        if arr1[l]<arr2[r]:
            res.append(arr1[l])
            l+=1
        else:
            res.append(arr2[r])
            r+=1
    if l!= len(arr1):
        res.extend(arr1[l:])
    if r!= len(arr2):
        res.extend(arr2[r:])
    arr1 = res[:len(arr1)]
    arr2 =res[len(arr1):]
    return arr1,arr2

#without extra space
def merge_array_1(arr1,arr2):
    m = len(arr1)-1
    n =0
    con=True
    while con:
        if arr1[m]>arr2[n]:
            arr1[m],arr2[n]=arr2[n],arr1[m]
            m-=1
            n+=1
        else:
            con =False
    return sorted(arr1),sorted(arr2)

if __name__=='__main__':
    #print(pascals(5))
    #print(majority_3_2([1,2,2,3,2]))
    #print(sum_3_two([-1,0,1,2,-1,-4]))
    #print(sum_4([1,0,-1,0,-2,2],0))
    #print(lon_sub([9, -3, 3, -1, 6, -5]))
    #print(xor_sub([4, 2, 2, 6, 4],6))
    #print(merge_int( [[1,7],[2,6],[8,10],[15,18]]))
    print(merge_array_1([1 ,4 ,8 ,10],[2, 3 ,9]))