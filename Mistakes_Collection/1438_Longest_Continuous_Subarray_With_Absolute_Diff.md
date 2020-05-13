# 1438


Test

```python
from collections import deque 

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxdeque = deque([])
        mindeque = deque([])
        res = 0
        
        for i in range(len(nums)):
            while maxdeque and nums[i] >= maxdeque[-1]:
                maxdeque.pop()
            maxdeque.append(nums[i])
            
            while mindeque and nums[i] <= mindeque[-1]:
                mindeque.pop()
            mindeque.append(nums[i])
            
            if maxdeque[0] - mindeque[0] <= limit:
                res = max(res, )
            76

```