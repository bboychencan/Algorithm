from collections  import deque
from typing import List

class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		maxdeque = deque([])
		mindeque = deque([])

		res = 0
		l = 0

		for i in range(len(nums)):
			while maxdeque and maxdeque[-1] < nums[i]:
				maxdeque.pop()
			maxdeque.append(nums[i])

			while mindeque and mindeque[-1] > nums[i]:
				mindeque.pop()
			mindeque.append(nums[i])

			while maxdeque and mindeque and maxdeque[0] - mindeque[0] > limit:
				if maxdeque[0] == nums[l]:
					maxdeque.popleft()
				if mindeque[0] == nums[l]:
					mindeque.popleft()
				l += 1


			res = max(res, i - l + 1)
			print(l, i, res)

		return res




s = Solution()
res = s.longestSubarray([4,2,2,2,4,4,2,2], 0)
print(res)
# 4 2 2 2 4 4 2 2
# 0

