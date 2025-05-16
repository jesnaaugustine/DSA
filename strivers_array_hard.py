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
            

if __name__=='__main__':
    #print(pascals(5))
    #print(majority_3_2([1,2,2,3,2]))
    print(sum_3_two([-1,0,1,2,-1,-4]))