from typing import List
import heapq
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = nums[::]
        res = nums[-1]
        delete = set()
        q = []
        heapq.heappush(q, (- dp[-1], n-1))
        for i in range(n-2, -1, -1):
            while q:
                if q[0][1] in delete:
                    heapq.heappop(q)
                else:
                    break
            if q:
            	dp[i] = max(dp[i], nums[i] - q[0][0])
            	print('here', dp[i], q[0], nums[i])
            	heapq.heappush(q, (-dp[i], i))
            if i+k < n:
                delete.add(i+k)
            res = max(dp[i], res)
        print(dp)
        return res


s = Solution()
res = s.constrainedSubsetSum([10,-2,-10,-5,20], 2)
print(res)