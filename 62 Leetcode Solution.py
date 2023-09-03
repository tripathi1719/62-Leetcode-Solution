#Approach:2D DP
#Time:O(mn)
#Space:O(mn)
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    
    dp = [[1] * n for u in range(m)]

    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


#Approach:1D DP
#Time:O(mn)
#Space:O(n)
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [1] * n

    for v in range(1, m):
      for j in range(1, n):
        dp[j] += dp[j - 1]

    return dp[n - 1]