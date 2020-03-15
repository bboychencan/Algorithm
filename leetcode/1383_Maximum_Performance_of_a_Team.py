# 1383. Maximum Performance of a Team
from typing import List
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = zip(speed, efficiency)
        arr = sorted(arr, key=lambda x: -x[1])
        res = 0
        queue = []
        cur = 0
        ssum = 0
        while cur < n:
            heapq.heappush(queue, arr[cur][0])
            ssum += arr[cur][0]
            if len(queue) <= k:
                res = max(res, ssum * arr[cur][1])
            else:
                ssum -= heapq.heappop(queue)
#                 print(temp, res)
                res = max(res, ssum * arr[cur][1])
            cur += 1
        return res % (10**9 + 7)                
                

# 这一次周赛，这道题猛一看觉得很简单，直接就开始套背包算法。
# 写完之后多次测试错误，才发现原来转移方程并不对。然后就蒙了。
# 看了答案，发现很多人都挂在这了。 这里用到了一种很巧妙的方法取分解这个问题，用efficiency来逐步把问题剥离开。
# 另外在计算speed之和的时候，为了避免重复计算，还需要用heapq，且每次只计算最顶端的值。

# 这一题整体来说非常的巧妙，说不上来属于什么题，可能是贪心？ 之前做过类似题目竟然没you想出来，看来能力还是不够啊