# 943. Find the Shortest Superstring (Travelling Salesman Problem)
# 这是一道旅行商问题，我想到了dfs的解法，但是dp解法没想到。
# 当时可能看了答案后清楚了，但是时隔4个月之后再次遇到的时候，我已经彻底忘了TSP还有dp解法。
# 感觉这类题目做的很少，我需要多练习几个


class Solution:
    def shortestSuperString(self, A: List[str]) -> str:
        # 首先，见到这种题可以很坦然，他的本质依然是dp，所以不难
        # 找到最优子结构，和状态转移方程，首先最优子结构就是求解并存储遍历任意m个节点的最优解
        # 然后扩展到m + 1的情况，一次类推即可。
        # 第二点是要注意存储最优路径。 然后就没什么太多难度了
        # 时间复杂度是 O(2**n * n * n)

        # 先用dp存储状态，“遍历m个节点，且最后节点为i"，定义最优子结构
        bitmax = 1 << len(A)
        dp = [[0 for i in range(len(A))] for i in range(bitmax)]
        path = [0 for i in range(bitmax]

        # 初始状态
        dp[0][0] = float('inf')
        # 状态转移方程
        dp[i][j] = min(dp[i][j], dp[i - (1<<j)][k], 0<k<n)

        # bottom up递推所有的值
        for i in range(bitmax):
            mini = float('inf')
            for j in range(len(A)):
                if i & (1 << j):
                    for k in range(len(A)):
                        if k & (i - 1<<j):
                            temp = dp[i - (1<<j)][k] + distance(s[k], s[j])
                        if dp[i][j] > temp:
                            dp[i][j] = temp
                    if dp[i][j] < mini:
                        path[i] = i - (1<<j)

        code = bitmax - 1
        res = []
        while code > 0:
            pre = path[code]
            i = math.lg(pre ^ code, 2)
            res = [s[i]] + res
            code = pre

        return res

        # 一些小技巧
        # bitmax的性质，很巧妙的处理了循环中的index
        # 注意初始化dp，对于每个单一字符串，取其长度为dp值
        # 注意循环计算dp时，从bit值1开始

