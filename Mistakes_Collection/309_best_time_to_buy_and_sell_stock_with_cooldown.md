# 309 

这一题四年前做不出来， 一直没有思路。

2020/05/13 再看这道题目的时候，很快有了思路，应该就用dp，只是dp的转移方程稍微需要思考一下。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        if n <= 0: return 0
        
        
        for i in range(n-1, -1, -1):
            mini = prices[i]            
            for j in range(i+1, n):
                dp[i] = max(dp[i], prices[j] - mini)
                mini = min(prices[j], mini)
                if j + 2 < n:
                    dp[i] = max(dp[i], dp[i] + dp[j+2])
        return dp[0]
            
```