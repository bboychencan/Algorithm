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
    