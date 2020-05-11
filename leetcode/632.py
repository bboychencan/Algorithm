
# TLE 解法 naive two pointers
from collections import Counter

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = [[] for i in range(2*10**5 + 1)]
        s = float('inf')
        t = - float('inf')

        k = len(nums)
        for i in range(k):
            for j in nums[i]:
                arr[j + 10 ** 5].append(i)
                s = min(s, j + 10 ** 5)
                t = max(t, j + 10 ** 5)

        l = s
        r = s-1
        levs = set()
        counter = Counter()        
        mini = float('inf')
        res = []
        while len(levs) < k:
            r += 1
            counter += Counter(set(arr[r]))
            levs |= set(arr[r])
        
        # print(r, levs)
        
        ok = True
        while l < r and ok:
            temp = Counter(set(arr[l]))
            for key in temp:
                if counter[key] - temp[key] <= 0:
                    ok = False
                    break
            else:
                counter -= temp
                l += 1
                
        res = [l, r]
        mini = r - l
        
        # print(res)
        while r < t:
            r += 1
            counter += Counter(set(arr[r]))
            ok = True
            while l < r and ok:
                temp = Counter(set(arr[l]))
                for key in temp:
                    if counter[key] - temp[key] <= 0:
                        ok = False
                        break
                else:
                    counter -= temp
                    l += 1
            if r - l < mini:
                mini = r - l
                res = [l, r]

        return [res[0] - 10 ** 5, res[1] - 10 ** 5]


# 看了答案看到有一种非常巧妙的heap解法，看起来似乎不难，但是不知道为什么自己就想不出来。
# 看完很沮丧
# 再仔细想了下，发现这是一个非常标准的叫做k路归并的问题的一个变形，而我对k路归并问题并没有
# 很熟悉，不能够做到迅速想出minheap的解法，这个可能是原因所在，脑子里一直在想BIT，线段树，
# 发现怎么也套不进去。