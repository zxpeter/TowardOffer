class Solution:
    def countDigitOne(self, n):
        count = 0
        for num in range(1, n+1):
            while num != 0:
                if num % 10 == 1:
                    count += 1   
                num //= 10
        return count

从1到n，每增加1，weight就会加1，当weight加到9时，再加1又会回到0重新开始。那么weight从0-9的这种周期会出现多少次呢？这取决于n的高位是多少，看图： 


以534为例，在从1增长到n的过程中，534的个位从0-9变化了53次，记为round。每一轮变化中，1在个位出现一次，所以一共出现了53次。 
再来看weight的值。weight为4，大于0，说明第54轮变化是从0-4，1又出现了1次。我们记1出现的次数为count，所以： 
count = round+1 = 53 + 1 = 54

如果此时weight为0（n=530），说明第54轮到0就停止了，那么： 
count = round = 53
--------------------- 
   
若weight为0，则1出现次数为round*base
若weight为1，则1出现次数为round*base+former+1
若weight大于1，则1出现次数为rount*base+base

class Solution:
    def countDigitOne(self, n):
        if n < 1:
            return 0
        count = 0
        base = 1
        num = n
        while num > 0:
            current = num % 10
            num //= 10
            count += base * num
            if current == 1:
                count += n % base + 1
            elif current > 1:
                count += base
            base *= 10
        return count
                
class Solution:
    def countDigitOne(self, n):
        if n < 1:
            return 0
        n = 785012
        count = 0
        base = 1
        num = n
        while num > 0:
            current = num % 10
            num //= 10
            count += base * (num-1)
            if current == 0:
                count += n % base + 1
            elif current > 0:
                count += base
            base *= 10
        return count          
        
