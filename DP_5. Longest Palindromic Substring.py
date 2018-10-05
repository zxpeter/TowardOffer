# longestPalindromeSubseq 子序列
class Solution(object):
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]

# longestPalindromeSubstring 子串
# o(n^2)的解法，原本需要o(n^3)，先生成每个子串，然后比较
class Solution(object):
    def longestPalindrome
    (self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            temp = self.palindrome(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.palindrome(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res
        
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1:r]
            
  # 求字串的所有子序列
  def printAllSubsquence(test, i, res):
      if i == len(test):
          print(res)
          return
      printAllSubsquence(test, i+1, res)              # 当前位置字符不加入
      printAllSubsquence(test, i+1, res + [test[i]])    # 当前位置字符加入

  # 求字串的所有子串
  def cut(s):
      results = []
      # x + 1 表示子字符串长度
      for x in range(len(s)):
          # i 表示偏移量
          for i in range(len(s) - x):
              results.append(s[i:i + x + 1])
      return results    
            
            
            
