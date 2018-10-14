# 10. Regular Expression Matching

def isMatch(self, s, p):
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True
    for i in range(1, len(p)):
        dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
    for i in range(len(p)):
        for j in range(len(s)):
            if p[i] == '*':
                dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                if p[i - 1] == s[j] or p[i - 1] == '.':
                    dp[i + 1][j + 1] |= dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
    return dp[-1][-1]
    
44. Wildcard Matching
dp[n] means the substring s[:n] if match the pattern i
dp[0] means the empty string '' or s[:0] which only match the pattern '*'
use the reversed builtin because for every dp[n+1] we use the previous 'dp'

class Solution:
  # @return a boolean
  def isMatch(self, s, p):
      length = len(s)
      if len(p) - p.count('*') > length:
          return False
      dp = [True] + [False]*length
      for i in p:
          if i != '*':
              for n in reversed(range(length)):
                  dp[n+1] = dp[n] and (i == s[n] or i == '?')
          else:
              for n in range(1, length+1):
                  dp[n] = dp[n-1] or dp[n]
          dp[0] = dp[0] and i == '*'
      return dp[-1]
