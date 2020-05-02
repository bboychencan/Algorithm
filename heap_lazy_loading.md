# Heap lazy loading

5180. Constrained Subset Sum (1425. Constrained Subsequence Sum)

This problem requires me to maintain a max heap of a k-length moving window. Therefore, I need to remove the last element from the heap
whenever the window slides, however, it's not easy to determine whether the last element is the max value or not. which mean the heap.pop 
operation is not applicable to remove the last element. 

So, we need to use an operation to specificly remove a element from heap, but that is not efficient.

Today, I learned a smart way to do this, it's called "Lazy delete", we can use a set to keep track of the elements that we "have deleted",
but do not necessarily remove it from the heap. We continue to use the max value on demand. But we check if the max value is in the "have deleted"
set constantly. Whenever we found that value is "deleted", we pop until we find another "max" value which is not deleted. This strategy free us
to find the specific element in heap and remove. Very Smart!!

```python
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
            	# print('here', dp[i], q[0], nums[i])
            	heapq.heappush(q, (-dp[i], i))
            if i+k < n:
                delete.add(i+k)
            res = max(dp[i], res)
        # print(dp)
        return res
```

# 单调队列优化dp
这种方法时间复杂度更低O(n), 更加优美