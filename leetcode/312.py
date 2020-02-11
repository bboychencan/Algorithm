class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[-1 for i in range(len(nums))] for i in range(len(nums))]
        if len(nums) == 1: return nums[0]
        n = len(nums)
        # calculate the case that i is the last burst ballon
        
        def recur(start, end):
            if start > end:
                return 0
            elif dp[start][end] != -1:
                return dp[start][end]
            elif start == end:
                if start == 0: 
                    dp[start][end] = nums[0] * nums[1]
                    return dp[start][end]
                if end == n - 1: 
                    dp[start][end] = nums[-1] * nums[-2]
                    return dp[start][end]
                else:
                    dp[start][end] = nums[start - 1] * nums[start] * nums[start + 1]
                    return dp[start][end]
            elif start < end:
                for i in range(start, end + 1):
                    left = nums[start - 1] if start >= 1 else 1
                    right = nums[end + 1] if end < n - 1 else 1
                    dp[start][end] = max(dp[start][end], recur(start, i-1) + recur(i + 1, end) + nums[i] * left * right)
                return dp[start][end]
        
        
        return recur(0, len(nums) - 1)


# 这道题一开始竟然想着把整个子数组序列组成的tuple作为key进行dp， 但一想这样肯定不行，肯定有更好的方法。一时没有想出来。
# 因为一开始的思路是把最开始burst的点作为分界点，但这样没法把结构分割成独立的两部分。没有思路
# 看了答案，发现有个巧妙的方法，利用最后一个burst的点作为分割点，这样左右两边是独立的两部分，而且可以写出转移方程。

# 上面是我看完之后根据自己的理解写的AC的答案，不过效率不高，而且代码有点丑，参考一下高票答案，有些地方可以改进

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 为了方便记录首位的特殊情况，可以讲nums的首尾拼接两个[1]
        nums = [1] + nums + [1]
        # 为了避免多次求len(nums)，可以先将长度值存下来
        n = len(nums)
        # dp可以直接用0初始化
        dp = [[0 for i in range(len(nums))] for i in range(len(nums))]
        
        def recur(start, end):
            # 数值0可以做bool变量使用，等于False
            # 关于边界的选取有技巧这里，start和end表示数组的外包，这样避免出现了边界start > end的情况
            if dp[start][end] or start + 1 == end:
                return dp[start][end]

            # 用coins作为临时变量存储
            coins = 0
            # 因为start end 为数组外包，因此可以只迭代内部元素
            for k in range(start + 1, end):
                coins = max(coins, recur(start, k) + recur(k, end) + nums[k] * nums[start] * nums[end])

            dp[start][end] = coins   
            return coins     
        
        return recur(0, n - 1)

# 经过这个修改，代码行数缩减将近一半


# 还有一种bottom-up的做法，我经常会不容易想出这个做法
这个bottom-up的方法不是那么容易想出来，暂时先放置