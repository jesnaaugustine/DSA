#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

###############
#bubble sort
def bubble_sort(arr):
    N= len(arr)
    while N>=0:
        ind = True
        for i in range(N-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                ind =False
        if ind:
            break;
        else:
            N -=1
    return arr

#############
# insertion sort
def insertion_sort(arr):
    n=1
    while n<len(arr):
        for i in range(n,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]= arr[i-1],arr[i]
            else:
                break;
        n +=1
    return arr
#############
#merge sort
def merge_sort(arr):
    if len(arr)==1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    l=0
    r=0
    result =[]
    while len(left) >l and len(right)>r:
        if left[l]<right[r]:
            result.append(left[l])
            l +=1
        else:
            result.append(right[r])
            r +=1
    if l<len(left):
        result.extend(left[l:])
    if r<len(right):
        result.extend(right[r:])
    return result

if __name__=='__main__':
    print(merge_sort([1,2,4,6,3,9,5]))