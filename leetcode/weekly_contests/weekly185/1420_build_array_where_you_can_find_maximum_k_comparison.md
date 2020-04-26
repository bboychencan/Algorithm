# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

这一道题，看完题目，大概10分钟左右有了思路，以及知道需要用dp with memoization来解答。
然后有了思路后开始写dfs，但是发现遇到了很多corner case，填填补补搞了半天没有完全理清楚。
感觉慢慢接近最终结果了，就又陷入了不断调试，error-driven的循环里，不知不觉30多分钟过去了。这道题本来是有信心做出来的，可是最终
还是失败。

看了一下大家的讨论，发现了自己的思路是没有问题的，可是问题出现在下面。
1. 状态转移方程没有完全想清楚
2. 想到的状态转移方法比较麻烦，有很多的corner case，然后一点点修修补补，时间很快就过去了。

我觉得下次遇到这样的情况，当对dp状态转移方程没有很强的把握的时候，可以先不要急着实现，慢慢把方程想清楚再开始会事半功倍。

正确的状态转移应该是，对于n,m,k, dp[n][m][k]，以这n个数的最后一个数作为边界。
case 1. 如果search cost在最后一个数之前达到了最大值k，也就是dp[n-1][m][k]，那么最后一个值可以有1-m种取法，m * dp[n-1][m][k]
case 2. 如果search cost在最后一个数达到了最大值k，也就是第n个数比前面n-1个数都大，那么根据前n-1数的最大值来分别讨论，
前n-1个数的最大值i可以是从1到m的任意一个，对于任意一种情况，dp[n-1][i][k-1]

```python

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[-1 for i in range(k+1)] for i in range(m+1)] for i in range(n+1)] 

        def dfs(arrlen, lgst, cost):
#             print(arrlen, lgst, cost)
            if dp[arrlen][lgst][cost] != -1:
                return dp[arrlen][lgst][cost]
            if arrlen == 1:
                dp[arrlen][lgst][cost] = 1 if cost == 1 else 0
                return dp[arrlen][lgst][cost]
            if cost == 0:					
                dp[arrlen][lgst][cost] = 0
                return 0
            else:
                res = 0
                for num in range(1, lgst):
                    res += dfs(arrlen-1, num, cost-1)
                res += dfs(arrlen-1, lgst, cost) * (lgst)
                dp[arrlen][lgst][cost] = res
                return res

        ans = 0
        for i in range(1, m+1):
            ans += dfs(n, i, k)
        return ans % 1000000007
    
```

看了排名前几的答案都是用了bottom-up的方法，不知道是因为效率更高还是实现起来更快。尝试自己写一下，对比一下。
```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

```
