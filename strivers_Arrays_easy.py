######
'''  
Covers medium and easy probles.
concept used:
1. Two pointers
2. xor property
3. prefix sum( to find longest subarry with sum k)
'''
#max of array
def max_array(arr):
    return max(arr)
#######
#second largest and smallest number in array:
#method 1: sorting arry
def sco_lar_smal(arr):
    if len(set(arr))<=1:
        return -1
    sor_arr = sorted(arr)
    print(sor_arr)
    s =1
    l = len(arr)-2
    ind_sml =False
    ind_lar =False
    while not ind_sml and not ind_lar:
        if sor_arr[s]!=sor_arr[s-1]:
            small = sor_arr[s]
            ind_sml =True

        else:
            s +=1
        if sor_arr[l] != sor_arr[l+1]:
            large = sor_arr[l]
            ind_lar=True
        else:
            l-=1
    return {'scod_small':small,'scod_large':large}
#method 2 :without sorting array
def sml_lrg(arr):
    if len(arr)<=1:
        return (-1,-1)
    sml = arr[0]
    s_sml =float('inf')
    lrg = arr[0]
    s_lrg = float('-inf')
    
    for i in range(1,len(arr)):
        if arr[i]<s_sml:
            s_sml,sml=arr[i],min(arr[i],sml)
        if arr[i]>s_lrg:
            s_lrg,lrg = lrg,max(arr[i],lrg)
    return (s_sml,s_lrg)
###########
#check if the array sorted
def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
###########
#remove duplicates in-place
def remove_dup(arr):
    l=0
    r =0
    while r<len(arr):
        if arr[l]!=arr[r]:
            l +=1
            arr[l] = arr[r]
        r+=1
    print(arr)
    return l+1

#############
#Left Rotate the Array by k position
def left_rotate(arr,k):
    if k>len(arr):
        k =k%len(arr)
    return arr[k:] +arr[:k]
###########
#Move all Zeros to the end of the array
def move_zero_left(arr):
    l =0
    r =1
    while r<len(arr):
        if arr[l]==0 and arr[r]!=0:
            arr[l],arr[r]=arr[r],arr[l]
            l =r-1
        if arr[l]!=0:
            l+=1
        r+=1
    return arr
########
#linear serch in array
#if found return zero based index else -1
def linear_search(arr,k):
    res =-1
    for i in range(len(arr)):
        if arr[i]==k:
            res =i
            break
    return res


############
#Union of Two Sorted Arrays
def union_sorted(arr1,arr2):
    l =0
    r =0
    res =[]
    while l<len(arr1) and r<len(arr2):
        if arr1[l]<arr2[r]:
            if arr1[l] not in res:
                res.append(arr1[l])
            l+=1
        elif arr1[l]>arr2[r]:
            if arr2[r] not in res:
                res.append(arr2[r])
            r+=1
        else:
            if arr1[l] not in res:
                res.append(arr1[l])
            l+=1
            r+=1
    if l !=len(arr1):
        for i in range(l,len(arr1)):
            if res[-1]!=arr1[i]:
                res.append(arr1[i])
    if r !=len(arr2):
        for i in range(r,len(arr2)):
            if res[-1]!=arr2[i]:
                res.append(arr2[i])
    return res

###########
#Find the missing number in an array
#method 1 - using sum formula
def missing_number(arr,N):
    a_sum = N*(N+1)/2
    arr_sum =sum(arr)
    return int(a_sum-arr_sum)

#method 2 - using xor property
#a^a =0
#a^0=a
def missing_number2(arr,N):
    a_xor =0
    arr_xor =0
    for i in range(N+1):
        a_xor =a_xor^i
    for j in arr:
        arr_xor ^=j
    return a_xor ^arr_xor


##########
#Count Maximum Consecutive One's in the array
def consecutive_one(arr):
    c =0
    l =0
    r =1
    while r<len(arr):
        if arr[l]!=1:
            l+=1
        else:
            if arr[r]!=1:  
                c =max(c,r-l)
                l = r  
        r+=1
    if arr[l]==1 and arr[r-1]==1:
        c = max(c,r-l)
    return c

###########
#Find the number that appears once, and the other numbers twice
#method 1- using dictionary
def one_number(arr):
    dict ={}
    for i in arr:
        dict[i] = dict.get(i,0)+1
    return [item[0] for item in dict.items() if item[1]!=2][0]

#method-2 - using xor property
def one_number1(arr):
    x_or =0
    for i in arr:
        x_or ^=i
    return x_or

#########
#Longest Subarray with given Sum K
def lon_sub_array(arr,k):
    c =0
    r=0
    c_sum = 0
    c_c =0
    while r<len(arr):
        c_sum +=arr[r]
        c_c +=1
        if c_sum ==k:
            c=max(c,c_c)
            c_sum=0
            c_c=0
            r+=1
        elif c_sum>k:
            if arr[r]==k:
                c=max(c,c_c)
            c_sum =0
            c_c =0
            r+=1
        else:
            r+=1
    return c
        
#method 2 - using prefix sum
def log_sub_arr_prefix(arr,k):
    dict ={}
    c_sum =0
    max_len =0
    for i in range(len(arr)):
        c_sum+=arr[i]
        if c_sum==k:
            max_len=max(max_len,i+1)
        rem = c_sum-k
        if rem in dict:
            max_len = max(max_len,i-dict[rem])
        dict[c_sum] = min(i,dict.get(c_sum,float('inf')))
    return max_len
#####
#Maximum Product Subarray in an Array
''' 
Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
'''
def max_prod(arr):
    max_p= float('-inf')
    prefix =1
    sufix =1
    for i in range(len(arr)):
        prefix *= arr[i]
        sufix *=arr[len(arr)-1-i]
        max_p= max(prefix,sufix,max_p)
        if prefix==0:
            prefix=1
        if sufix ==0:
            sufix=1
    return max_p


if __name__=='__main__':
    #print(remove_dup([1,1,2,2,2,3,3]))
    #print(left_rotate([1,2,3,4],5))
    #print(linear_search([0,0,0,5],4))
    #print(union_sorted([1,2,2,3,4],[2,4,5,6,7,8]))
    #print(missing_number2([1,2,3,5],5))
    #print(consecutive_one([0,1,1,0]))
    #print(one_number1([1,1,2,2,3,3,4,4,5]))
    #print(log_sub_arr_prefix([2,0,0,1,3],3))
    print(max_prod([1,2,-3,0,-4,-5]))