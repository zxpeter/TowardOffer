# maxSubArray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        maxcur = maxsum = nums[0]
        for item in nums[1:]:
            maxcur = max(maxcur+item, item)
            maxsum = max(maxsum, maxcur)
        return maxsum
        
# 198. House Robber

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )

class Solution:
    def rob(self, nums):
        last, now = 0, 0 
        for i in nums: last, now = now, max(last + i, now)       
        return now

class Solution2.1(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])

        return res[-1]
        
以上的代码需要O(N)空间，利用滚动数组可以实现O(1)空间, 滚动数组针对这一类的问题，当dependency只取决于k个数的时候，一种方法是可以定义k个函数来作为迭代的数据存储，另一种方法就是开辟一个长度为k的数组，然后在迭代的时候，更新对应的res[i%k]即可。
我比较喜欢这种方法的原因是，这种方法对应上面的方式，需要更改的不多，如果在面试时候仅仅想出了上面的代码，可以再不花多少时间的情况下，优化出O(1)的空间复杂度。      

class Solution2.2(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        
        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i%2] = max(res[(i-1)%2], res[(i-2)%2] + nums[i])

        return max(res[0], res[1])
        
# 213. House Robber II 

class Solution1.1(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])

        return res[-1]
        
class Solution1.2(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i%2] = max(res[(i-1)%2], res[(i-2)%2] + nums[i])

        return max(res[0], res[1])
        
        
