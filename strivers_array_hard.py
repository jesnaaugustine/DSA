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

if __name__=='__main__':
    print(pascals(5))