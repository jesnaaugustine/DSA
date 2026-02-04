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
#198. House Robber
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<2:
        return max(nums)
    dp=[0]*len(nums)
    dp[0]=nums[0]
    dp[1]= max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]
if __name__ =='__main__':
    print(climbStairs(3))
    nums =[1,2,3,1]
    print(rob(nums))
        