46. Permutations
Given a collection of distinct integers, return all possible permutations.
如果有重复，则在最后用set去重 set(result)
class Solution(object):
    def permute(self, nums):
        result = []
        ways = []
        if not nums:
            return []
        self.dfs(result, nums, ways)
        return result

    def dfs(self, result, nums, ways):
        if not nums:
            result.append(ways)
        for i in range(len(nums)):
            self.dfs(result, nums[:i]+nums[i+1:], ways+[nums[i]])
            
            
