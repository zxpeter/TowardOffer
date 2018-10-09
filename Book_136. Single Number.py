class Solution(object):
    def singleNumber(self, nums):
        if not nums:
            return 0
        a = 0
        for i in nums:
            a = a ^ i
        return a
        
class Solution(object):
    def singleNumber(self, nums):
        one = 0
        two = 0
        three = 0
        for i in range(0,len(nums)):
            two |= one & nums[i] #当新来的为0时，two = two | 0，two不变，当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
            one ^= nums[i]       #新来的为0，one不变，新来为1时，one是0、1交替改变
            three = one & two    #当one和two为1是，three为1（此时代表要把one和two清零了）
            one &= ~three        #把one清0
            two &= ~three        #把two清0
        return one      
        
class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        num1, num2 = 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

  
        
        
