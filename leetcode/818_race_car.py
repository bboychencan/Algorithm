import math
class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf') for i in range(2 * target + 1)]
        dist = 0
                
        def find(dist):
            # print(dp)
            if dp[dist] != float('inf'): 
                return dp[dist]
            n = dist.bit_length()
            if dist + 1 == 2 ** n:
                dp[dist] = n
                return dp[dist]
            else:
                dp[dist] = min(dp[dist], find(2**n - 1 - dist) + n + 1)
                for m in range(n - 1):
                    dp[dist] = min(dp[dist], find(dist - 2**(n-1) + 2**m) + 1 + n + m)
                return dp[dist]
        
        find(target)
#         print(dp)
        return dp[target]



# 以下的假设很关键，但是不知道如何证明
#1. 在超过target之前，汽车可以掉头，但只可能发生在离target最近的时候
#2. 在超过target之后，汽车需要立刻掉头。
#3. 在超过target之前，汽车掉头回跑的距离不会超过掉头前离target的距离

# 另外学到一个bit_length的用法，很方便