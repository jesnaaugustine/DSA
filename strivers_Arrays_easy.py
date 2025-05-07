######
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


if __name__=='__main__':
    #print(remove_dup([1,1,2,2,2,3,3]))
    #print(left_rotate([1,2,3,4],5))
    #print(linear_search([0,0,0,5],4))
    print(union_sorted([1,2,2,3,4],[2,4,5,6,7,8]))