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
##
def Training(nums):
    dp = nums[0]
    for i in range(1,len(nums)):
        dp_temp =[]
        for j in range(len(nums[i])):
            temp = [nums[i][j]+dp[k] for k in range(len(dp)) if j!=k]
            dp_temp.append(max(temp))
        dp = dp_temp
    return max(dp)
#62. Unique Paths
def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[1]*n
        for i in range(1,m):
            temp_dp = [0]*n
            temp_dp[0]=1
            for j in range(1,n):
                temp_dp[j]=temp_dp[j-1]+dp[j]
            dp =temp_dp
        return dp[-1]
def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        if obstacleGrid[0][0]==1 or len(obstacleGrid)==0:
            return 0
        dp =[1]+([0]*(len(obstacleGrid[0])-1))
        for i in range(len(obstacleGrid)):
            dp_temp = []
            if obstacleGrid[i][0]==1:
                dp_temp.append(0)
            else:
                dp_temp.append(dp[0])
            for j in range(1,len(obstacleGrid[i])):
                if obstacleGrid[i][j]==1:
                    dp_temp.append(0)
                else:
                    dp_temp.append(dp_temp[j-1]+dp[j])
            dp=dp_temp
        return dp[-1]
#64. Minimum Path Sum
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    dp =[]
    dp.append(grid[0][0])
    for i in range(1,len(grid[0])):
        dp.append(dp[i-1]+grid[0][i])
    #print(dp)
    for j in range(1,len(grid)):
        dp_temp=[]
        dp_temp.append(dp[0]+grid[j][0])
        for k in range(1,len(grid[j])):
            dp_temp.append(grid[j][k]+min(dp_temp[k-1],dp[k]))
        dp =dp_temp
    return dp[-1]
def minimumTotal(triangle):
    # Start from second last row
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(
                triangle[row + 1][col],
                triangle[row + 1][col + 1]
            )
    
    return triangle[0][0]

def minimumTotal_1(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp=triangle[0]
    for i in range(1,len(triangle)):
        dp_temp =[]
        dp_temp.append(dp[0]+triangle[i][0])
        for k in range(1,len(triangle[i])-1):
            dp_temp.append(triangle[i][k]+min(dp[k-1],dp[k]))
        dp_temp.append(dp[-1]+triangle[i][-1])
        dp=dp_temp
    return min(dp)
        
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
    matrix =[[70, 40, 10], [180, 20, 5], [200, 60, 30]]
    print(Training(matrix))
    print(uniquePaths(3,7))
    obstacleGrid =[[0,0,0],[0,1,0],[0,0,0]]      
    print(uniquePathsWithObstacles(obstacleGrid))
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minimumTotal_1(triangle))


        