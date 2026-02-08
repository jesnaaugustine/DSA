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
#213. House Robber II
def rob2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def robthis(nums):
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]= max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]
    if len(nums)<=2:
        return max(nums)
    temp1 =nums[:-1]
    temp2 = nums[1:]
    return max(robthis(temp1),robthis(temp2))
''' 
Problem Statement: Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1..
'''
def FrogJump(nums):
    if len(nums)==1:
        return 0
    if len(nums)==2:
        return abs(nums[0]-nums[1])
    prev2 = 0
    prev1 = abs(nums[0]-nums[1])
    for i in range(2,len(nums)):
        cur = min(prev1+abs(nums[i]-nums[i-1]),prev2+abs(nums[i]-nums[i-2]))
        prev2 = prev1
        prev1 =cur
    return prev1
def FrogJumpk(nums,k):
    if len(nums)==0:
        return 0
    dp =[]
    dp.append(0)
    for i in range(1,len(nums)):
        temp = float('inf')
        for j in range(1,k+1):
            if i-j==-1:
                break
            cur = abs(nums[i]-nums[i-j])+dp[i-j]
            temp = min(temp,cur)
        dp.append(temp)
    return dp[-1]

if __name__ =='__main__':
    print(climbStairs(3))
    nums =[1,2,3,1]
    print(rob(nums))
    print(rob2(nums))
    nums = [2,1,3,5,4]
    print(FrogJump(nums))
    heights = [15, 4, 1, 14, 15]
    k = 3
    print(FrogJumpk(heights,k))
        