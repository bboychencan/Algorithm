# 这里面除了BIT使用是一个难点外，还有一个难点就是对于二分查找边界的把控

import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0] * (len(nums)+1)
        presum[0] = 0
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        sortsum = sorted(set(presum))
        # sortsum = sorted(presum)
        c = [0] * (len(sortsum) + 1)
        mapp = {v: i for i,v in enumerate(sortsum)}
        
        def add(i):
            while i < len(c):
                c[i] += 1
                i += (i&-i)
        
        def count(i):
            res = 0
            while i >= 1:
                res += c[i]
                i -= (i&-i)
            return res
        
        def bs(x, start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            
        
        res = 0
        for i in range(len(presum)):
            high = presum[i] - lower
            low = presum[i] - upper
            sumcounth = count(bisect.bisect_right(sortsum, high) - 1 + 1)
            sumcountl = count(bisect.bisect_left(sortsum, low) -1 + 1)
            # print(sortsum,presum, presum[i], low, high, sumcounth, sumcountl)
            # print(high, low, bisect.bisect_right(sortsum, high), bisect.bisect_right(sortsum, low))
            # print(high, low, bisect.bisect_right(sortsum, high), bisect.bisect_left(sortsum, low))
            res += sumcounth - sumcountl
            # add(mapp[presum[i]] + 1)
            add(bisect.bisect_right(sortsum, presum[i]) - 1 + 1)
        return res