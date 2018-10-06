62. Unique Paths
class Solution(object):
    def uniquePaths(self, m, n):
        #         dp =[[1 for i in range(n)] for j in range(m)]
        #         for i in range(1, m):
        #             for j in range(1, n):
        #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #         return dp[-1][-1]
        r, c = m, n
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        dp[0][0] = 1
        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0]
        for i in xrange(1, n):
            dp[0][i] = dp[0][i-1]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])
        return dp[-1][-1]

63. Unique Paths II
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, r):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for i in xrange(1, c):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]   
        
64. Minimum Path Sum
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
     
