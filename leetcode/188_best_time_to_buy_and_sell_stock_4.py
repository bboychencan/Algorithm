class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(n)] for i in range(k + 1)]
        if len(prices) < 2 or k == 0:
            return 0
        
        if k >= n / 2:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        
        for i in range(1, k + 1):
            localmax = dp[i-1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + localmax)
                localmax = max(localmax, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]
                
# 这一题感觉有点奇怪，上面的方法看似最优，但是仍然超时，用java写的同样的内容就可以通过。不知道是不是python太慢了的缘故。