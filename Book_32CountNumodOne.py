class Solution:
    def countDigitOne(self, n):
        count = 0
        for num in range(1, n+1):
            while num != 0:
                if num % 10 == 1:
                    count += 1   
                num //= 10
        return count
        
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
        
