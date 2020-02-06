class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = {}
        def recur(pos, k):
            print(pos, k)
            # 习惯将这种简单的if判断变为一行
            # 对于python里的dict类型，可以直接用dp[pos, k]来存储tuple，等价于dp[(pos, k)]!
            if (pos, k) in dp: return dp[pos, k]
            if k < 1  or len(A) - k < pos:
                return -1
            elif pos == len(A) - 1:
                dp[(pos, k)] = A[pos]
                return dp[(pos, k)]
            elif k == 1:
                dp[pos, k] = sum(A[pos:]) / len(A[pos:])
                return dp[pos, k]
            else:
                # 把临时变量temp = -1去掉，直接用dp[pos, k] 
                # 用临时变量cur存储前若干项和，直接给dp[pos, k]赋值
                cur, dp[pos, k] = 0, 0
                for i in range(1, len(A) - pos - k + 2):
                    # 这一步的sum也可以简化
                    dp[pos, k] = max(dp[pos, k], sum(A[pos:pos+i]) / len(A[pos:pos+i]) + recur(pos + i, k - 1))
                    # newmax = recur(pos + i, k - 1)
                    # if newmax != -1:
                        # temp = max(temp, newmax + sum(A[pos:pos+i]) / len(A[pos:pos+i]))

                return dp[pos, k]
        
        return recur(0, K)


# 这道题看完之后就觉得是基本的dp题，不难，但是边界研究那个边界case花的时间比较多
# 另外稍微对比了一下高票答案，发现很多可以改进的地方，包括代码格式等。