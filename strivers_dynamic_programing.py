#70. Climbing Stairs
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n <=2:
        return n
    prev2 =1
    prev1 =2
    for i in range(2,n):
        temp = prev1+prev2
        prev2=prev1
        prev1 =temp
    return prev1


if __name__ =='__main__':
    print(climbStairs(3))
        