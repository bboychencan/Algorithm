class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        if n == d: return sum(jobDifficulty)
    
        dp = [[1005 for i in range(d+1)] for i in range(n)]
        
        def recur(i, k):
            if dp[i][k] != 1005: return dp[i][k]
            if n - i == k and k > 0:
                dp[i][k] = sum(jobDifficulty[i:])
            elif k == 1:
                dp[i][k] = max(jobDifficulty[i:])
            else:
                minimum = 1005 * 300
                maxd = 0
                for cur in range(i, n-k+1):
                    # 这个地方只比较下一个值，减少了计算量
                    maxd = max(maxd, jobDifficulty[cur])
                    minimum = min(minimum, recur(cur+1, k-1) + maxd)
                dp[i][k] = minimum
            return dp[i][k]
        
        return recur(0, d)

# 这一道题跟1278属于同类题目，基本上很快有了思路。
# 提交答案的时候反而错了两次， 原因是这次用了二维数组存储dp，其中关于k的边界判定忘记考虑了进去。
# 初次AC的结果速度只超过了3%，看了一下别人的答案，发现是在上面求max的时候可以简化，没有必要每次把当前数组全部计算一遍，这样大大降低了时间
# 同时跟@lee215 学到了一个方法，@functools.lru_cache(None)， 使用他可以不用自行做dp存储，这个功能以前不了解，可以研究一下。