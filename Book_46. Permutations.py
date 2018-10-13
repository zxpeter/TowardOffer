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
            
            
179. Largest Number     
Given a list of non negative integers, arrange them such that they form the largest number.
Input: [10,2]
Output: "210"           
    
class Solution:
    def largestNumber(self, nums): # python 2.7 have cmp, which no longer in py3
        str_num = map(str, nums)
        str_num.sort(cmp=lambda x,y: cmp(x+y, y+x),reverse = True)
        return str(int(''.join(str_num)))  # 解决了‘00’ -> ‘0’ 的问题
        
        
