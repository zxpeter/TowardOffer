class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        max_step = 0
        for i in range(len(nums)):
            if max_step < i:
                return False
            max_step = max(max_step, i + nums[i])
        return max_step >= len(nums) - 1
        
  class Solution2:
    def canJump(self, nums):
        stepsLeft = nums[0]
        if not stepsLeft and len(nums) > 1:
            return False

        for num in nums[1:-1]:
            stepsLeft = max(stepsLeft - 1, num)
            if not stepsLeft:
                return False
        return True
        
        
45. Jump Game II, minimum number of jumps.
class Solution(object):
def jump(self, nums):
    res = 0
    edge = 0
    maxEdge = 0
    for i in range(len(nums)):
        if i > edge:
            edge = maxEdge
            res += 1
        maxEdge = max(maxEdge,i+nums[i])
    return res



