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
#############
#Peak element in Array
'''  
roblem Statement: Given an array of length N. Peak element is defined as the element greater than both of its neighbors. Formally, if 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

Note: For the first element, the previous element should be considered as negative infinity as well as for the last element, the next element should be considered as negative infinity.
https://takeuforward.org/data-structure/peak-element-in-array/
Example 1:
Input Format: arr[] = {1,2,3,4,5,6,7,8,5,1}
Result: 7
Explanation: In this example, there is only 1 peak that is at index 7.

'''
def peak_element(arr):
    if len(arr)==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[-1]>arr[-2]:
        return len(arr)-1
    l = 1
    r = len(arr)-2
    while l<=r:
        m =(l+r)//2
        if arr[m]>arr[m-1] and arr[m]>arr[m+1]:
            return m
        elif arr[m-1]<arr[m]:
            l =m+1
        else:
            r =m-1
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


#############
#Find the Smallest Divisor Given a Threshold
'''
Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value.

Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

'''
def smallest_divisor(arr,limit):
    l = 1
    r = max(arr)
    result = max(arr)
    while l<=r:
        mid =(l+r)//2
        ans =0
        for i in arr:
            ans+= (i//mid if i%mid ==0 else (i//mid)+1)
        if ans >limit:
            l =mid+1
        else:
            result =min(result,mid)
            r=mid-1
    return result
##############
#Capacity to Ship Packages within D Days
'''  
Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within 'd' days.
The weights of the packages are given in an array 'of weights'. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship.
Find out the least-weight capacity so that you can ship all the packages within 'd' days.

Example 1:
Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
Result: 9
Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
Day         Weights            Total
1        -       5, 4          -        9
2        -       5, 2          -        7
3        -       3, 4          -        7
4        -       5              -        5
5        -       6              -        6
So, the least capacity should be 9.
'''      
def days_check(arr,c):
    cur_c =0
    day =1
    for i in arr:
        cur_c +=i
        if cur_c ==c:
            day +=1
            cur_c =0
        elif cur_c>c:
            day+=1
            cur_c =i
    return day
def min_capacity(arr,d):
    l = max(arr)
    r = sum(arr)
    ans = sum(arr)
    while l<=r:
        mid = (l+r)//2
        day = days_check(arr,mid)
        if day>d:
            l = mid+1
        else:
            ans = min(ans,mid)
            r = mid-1
    return ans
###########
#Kth Missing Positive Number

'''  
Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

Example 1:
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
Example 2:
Input Format: vec[]={4,7,9,10}, k = 4
Result: 5
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.
'''
#Brute force
def missing_number(arr,k):
    prev =0
    cur_missing =0
    for a in arr:
        temp =cur_missing +a-prev-1
        if temp<k:
            cur_missing =temp
            prev = a
        else:
            ans = prev+k-cur_missing
            return ans
    return -1
def missingK1(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1  # shifting k
        else:
            break
    return k
######Binary search
def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

############
#Find the row with maximum number of 1's
'''  
Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
Your task is to find the index of the row with the maximum number of ones.
Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1.

Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).

'''
def max_ones(arr):
    n  =len(arr)
    m =len(arr[0])
    max_cnt = 0
    max_idx =-1
    for i in range(n):
        l =0
        r = m-1
        temp = m
        while l<=r:
            mid =(l+r)//2
            if arr[i][mid]==1:
                r=mid-1
                temp =min(temp,mid)
            else:
                l =mid+1
        if max_cnt<m-temp:
            max_cnt = m-temp
            max_idx = i
    return max_idx
############
#Search in a sorted 2D matrix
'''  
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.
Example 1:
Input Format: N = 3, M = 4, target = 8,
mat[] = 
1 2 3 4
5 6 7 8 
9 10 11 12
Result: true
Explanation: The ‘target’  = 8 exists in the 'mat' at index (1, 3).
'''
#method 1 - traverse through all rows, if traget in that row then do BS only in that row (O(N+log(m)))
def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        if arr[i][0]<=target and arr[i][-1]>=target:
            l = 0
            r = m-1
            while l<=r:
                m = (l+r)//2
                if arr[i][m]==target:
                    return True
                elif arr[i][m]<target:
                    l = m+1
                else:
                    r=m-1
    return False
#method 2- convert 2D to 1D. if we do it complexity will be high instead of that take l =0 and r = n*m, and convert mid to [n][m]
def search_2D_optimized(arr,target):
    n = len(arr)
    m = len(arr[0])
    l =0
    r = n*m-1
    while l<=r:
        mid = (l+r)//2
        row = mid//m
        col = mid%m
        if arr[row][col]==target:
            return True
        elif arr[row][col]<target:
            l =mid+1
        else:
            r = mid-1
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
    #print(bs_rotated([7, 8, 1, 3, 3, 3, 4, 5, 6],2))
    #print(min_rotated([4,5,6,7,0,1,2,3,3]))
    #print(rotation_count([3,4,5,6,7,0,1,2,3]))
    print(peak_element([1,2,3,4,5,6,7,8,5,1]))

    ###BS on Answers
    #print(single_ele([1,2,2,3,3,4,4,5,5,6,6]))
    #print(sqrt(36))
    #print(minEatingSpeed([30,11,23,4,20],6))
    #print(bouquet_make([1, 10, 3, 10, 2],2,3))
    #print(smallest_divisor([8,4,2,3],10))
    #print(min_capacity([1,2,3,4,5,6,7,8,9,10],1))
    ###BS on 2D array
    #print(missingK([4,7,9,10],4,5))
    #print(max_ones([[0,0,0,0]]))

    #print(search_2D_optimized([[1,2,3,4],[5,6,7,8],[9,10,11,13]],0))