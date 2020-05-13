# 336

这道题3个月前和6个月前都尝试过，失败了。 2020/05/13 又尝试了一下，发现不难，只要用hashmap存储一下某些前缀即可，写完后稍微调试了一下就AC了，感觉这段时间还是有进步的看来。

```python
from typing import List
from collections import defaultdict
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        A = defaultdict(list)
        B = defaultdict(list)
        for i, w in enumerate(words):
            A[w].append(i)
            s = 0
            e = 0
            while e < len(w):
                t1 = s
                t2 = e
                while w[t1] == w[t2] and t1 < t2:
                    t1 += 1
                    t2 -= 1
                if t1 >= t2:
                    B[w[e+1:]].append(i)
                e += 1
        
        res = []
        for i, w in enumerate(words):
            # print(i, w, A[w[::-1]])
            for j in A[w[::-1]]:
                if i != j:
                    res.append([i, j])
            for j in B[w[::-1]]:
                if i != j:
                    res.append([i, j])
            
            e = len(w) - 1
            s = len(w) - 1


            while s >= 0:
                t1 = s
                t2 = e
                while w[t1] == w[t2] and t1 < t2:
                    t1 += 1
                    t2 -= 1
                if t1 >= t2:
                    temp = w[s-1::-1] if s >= 1 else ""
                    # print(i, w, s, s-1, w[s-1::-1], A[w[s-1::-1]], B[w[s-1::-1]])
                    for j in A[temp]:
                        if i != j:
                            res.append([i, j])
                s -= 1
        return res
```