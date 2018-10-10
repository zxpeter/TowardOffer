
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = numbers[0]
        count = 1
        for num in numbers[1:]:
            if count == 0:
                count = 1
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        #check if numbers do have item more than half
        times = 0
        for i in numbers:
            if i == res:
                times += 1
        if times <= len(numbers) / 2:
            res = 0
        
        return res
# [1,2,3,2,2,2,5,4,2]
        
        
        
        
        
