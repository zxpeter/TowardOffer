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
        
        
39. Combination Sum
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        res = []
        path = []
        candidates.sort()
        self.dfs(res, candidates,0, path, target)
        # for item in res:
        #     item.sort()
        # res = list(set(tuple(item) for item in res))
        return res
        
    def dfs(self, res, candidates, index, path, target):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            # if candidates[i] <= target:
            self.dfs(res, candidates, i, path+[candidates[i]], target-candidates[i])
                


40. Combination Sum II
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        res = []
        path = []
        candidates.sort()
        self.dfs(res, candidates,0, path, target)
        # for item in res:
        #     item.sort()
        # res = list(set(tuple(item) for item in res))
        return res
        
    def dfs(self, res, candidates, index, path, target):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            # if candidates[i] <= target:
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(res, candidates[:i]+candidates[i+1:], i, path+[candidates[i]], target-candidates[i])
                


