# 300. Longest Increasing Subsequence

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
        
# 673. Number of Longest Increasing Subsequence
      
class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1]*len(nums)
        count = [1]*len(nums)
        
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                    elif dp[i] == dp[j]+1:
                        count[i] += count[j]
                
        return sum([count[i] for i in range(len(nums)) if dp[i] == max(dp)])

674. Longest Continuous Increasing Subsequence   
class Solution(object):
    def findLengthOfLCIS(self, nums):
        # Time: O(n)
        # Space: O(1)
        max_len = i = 0
        while i < len(nums):
            curr = 1
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr, i = curr + 1, i + 1
            max_len = max(max_len, curr)
            i += 1
        return max_len  
    
392. Is Subsequence    
class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False  
