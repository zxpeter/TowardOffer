# 121. Best Time to Buy and Sell Stock
该题解法和最大连续子数组和的解法思路是一样的。
1、根据股票的利益意义，想要更多利益则值低时买进，值高时卖出。
根据提供的股票价格不方便得出股票价格变化，对原数据进行计算：list[i] - list[i-1] = 股票的变化。
变化为正时股票增长（存在利益），变化为负时股票为下跌（无利益）。
2、得到股票的变化值列表，即求最大子数组和，最后得到正解。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int [7,1,5,3,6,4]
        """
        if not prices:
            return 0
        max_pro = 0
        min_price = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
        return max_profit

122. Best Time to Buy and Sell Stock II, You may complete as many transactions as you like 贪心
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = []
        for i in range(len(prices) - 1):
            pro.append(max(prices[i + 1] - prices[i], 0))
        return sum(pro)


123. Best Time to Buy and Sell Stock III,  You may complete at most two transactions.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        profits = []
        # forward 
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            profits.append(max_profit)
            
        # backward
        max_price = prices[-1]
        max_profit = 0
        max_res = 0
        for i in range(len(prices)-1, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            max_res = max(max_profit + profits[i], max_res)
                  
        return max_res

# with K transaction
def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    # k is big enougth to cover all ramps.
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in xrange(k + 1)]
    for i in xrange(1, k + 1):
        # The max profit with i transations and selling stock on day j.
        localMax = [0] * n
        for j in xrange(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day (j - 1)
                # and sell it on day j.
                globalMax[i - 1][j - 1] + profit,
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day j and
                # sell it on the same day, so we have 0 profit, apparently
                # we do not have to add it.
                globalMax[i - 1][j - 1],  # + 0,
                # We have made profit in (j - 1) days.
                # We want to cancel the day (j - 1) sale and sell it on
                # day j.
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]
	
	

309. Best Time to Buy and Sell Stock with Cooldown
第一感觉就是动态规划，但是还是难以将抽象的题目具体化，如何根据前面的状态推断现在这个状态（状态转移方程）。 
根据题意可以明了，总共有三个状态，持有股票，卖掉股票，休息一天，后两种都可以归纳为未持有股票。状态有了，如何推断？ 
再往下分析，未持有股票的状态，最大利润有两种可能。一，和昨天一样保持未持有；二，昨天持有股票今天卖掉
sdp[i] = Math.max(sdp[i-1],bdp[i-1] + prices[i]);1
持有股票的状态，最大利润也有两种可能。一，和昨天一样持有股票不卖；二，两天前未持有（休息一天）今天购买。
bdp[i] = Math.max(bdp[i-1],sdp[i-2] - prices[i]);

def maxProfit(self, prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell
    
714. Best Time to Buy and Sell Stock with Transaction Fee
相当于降低卖价或者提升买价，对profit做相应调整即可  
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(2)] for _ in xrange(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in xrange(1, len(prices)):
            dp[i][1] = max([dp[i - 1][0] - prices[i], dp[i - 1][1]])
            dp[i][0] = max([dp[i - 1][1] + prices[i] - fee, dp[i - 1][0]])

        return dp[-1][0]
    
    
    
    
    
                         
