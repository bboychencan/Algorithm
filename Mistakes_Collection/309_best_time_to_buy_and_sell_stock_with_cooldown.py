from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        if n <= 0: return 0
        
        for i in range(n-1, -1, -1):
            mini = prices[i]            
            for j in range(i+1, n):
                temp = prices[j] - mini
                dp[i] = max(dp[i], temp)
                mini = min(prices[j], mini)
                if j + 2 < n:
                    dp[i] = max(dp[i], temp + dp[j+2])
        print(dp)
        return dp[0]

s = Solution()
res = s.maxProfit([6,1,3,2,4,7])
print(res)