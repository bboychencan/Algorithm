class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[105 for i in range(k+1)]
               for i in range(n)] 
              for i in range(n)]
        
        def minchange(i, j):
            if i == j: return 0
            count = 0
            while i < j:
                if s[i] != s[j]: count += 1
                i += 1
                j -= 1
            return count 
        
        def recur(i, j, num):
            if dp[i][j][num] < 105: return dp[i][j][num]
            if j - i == num - 1: 
                dp[i][j][num] = 0
            elif num == 1:
                dp[i][j][num] = minchange(i,j)
            else:
                minimum = 105
                for cur in range(i, j - num + 2):
                    minimum = min(minimum, recur(cur + 1, j, num-1) + recur(i, cur, 1))
                dp[i][j][num] = minimum
                
            return dp[i][j][num]
        
        return recur(0, n-1, k)

# 这道题看完，5分钟内有了思路，然后大概不到20分钟写完，提交一次性通过，感觉蛮有成就感，尤其是这题是hard
# 总结一下，这里面吸取了教训，将常量n存了下来，同时dp的存储采用三维数组而非dict，最后关于递归里面的逻辑判断，尽量简洁统一。
# 最后，这道题的难点是关于边界情况的确定