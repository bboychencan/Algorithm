import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        dp[0] = [[]]
        for num in candidates:
            for i in range(num, target + 1):
                temp = [j + [num] for j in dp[i-num]]
                dp[i].extend(temp)
        return dp[target]

# 这一题是做805. Split Array With Same Average的时候被人提及的，4年前做过，重新回做一次。
# 看了一下，觉得这是标准的完全背包问题，很快写了个dp，不过因为需要返回的是所有的排列，因此在dp中如何存储数据花了会时间思考。
# 本来用的是直接用temp = dp[i]的方法，但是报错，发现是因为python里的数组直接赋值得到的是引用，会修改之前的结果
# 用了copy模块，deepcopy了一下。然后发现还是不对，然后注意到一开始dp的初始化有问题，dp = [[]] * (target + 1)这种初始化方法，数组中的值指向同一个地址，因此修改的时候出错。
# 改成了[[] for i in range(target + 1)] 就AC了。
# 不过参考了一下别人的答案，发现善用python 的comprehension很有用。不用deepcopy，直接temp = [j + [num] for j in dp[i-num]] 大大提升了效率。