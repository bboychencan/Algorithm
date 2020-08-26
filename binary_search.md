# Binary Search


## 2020/08/16
二分查找很好用，可以将O(n)的复杂度降到O(log(n))，使用二分一般是在单调有序的场景下。
如何能够识别出问题的单调有序属性是使用二分法的关键。 以前总觉得这类问题很简单，没有专门整理，可是这次周赛又挂在第三道medium
题上了，我本来尝试用dp，但是总是TLE。 
1552 https://leetcode.com/problems/magnetic-force-between-two-balls/

在这里专门整理一下，以后遇到类似的题目，要能够想到这个方法。
这篇讲解整理的很好，https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems


## Most Generalized Binary Search
Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:
Minimize k , s.t. condition(k) is True

```
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

## 进阶版
这个是我2020/08/16周赛跪的地方）
有些问题不是很冥想，第一眼很难想到用二分去求解。more often are the situations where the search space and search target are not so readily available. we might just turn to dynamic programming or DFS and get stuck for a very long time.

这个时候怎么知道可以用二分，As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- https://leetcode.com/problems/split-array-largest-sum/ （这题之前试过，总是TLE，放弃了。。。）
- https://leetcode.com/problems/koko-eating-bananas/submissions/
- https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/ （这道题AC了，但是不确定当时是不是看答案AC的）
- https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/ （这道题挂了很多次）


- 1300 Sum of Mutated Array Closest to Target https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
这一题有很明显的单调递增属性，而且也是要求最小值
- 410 Split Array Largest Sum https://leetcode.com/problems/split-array-largest-sum/ 
这一题和08/16周赛的题很想，知道这道题可以用二分后，很快就可以有思路


- 719 Find K-th Smallest Pair Distance https://leetcode.com/problems/find-k-th-smallest-pair-distance/
2020/08/26
这一道题很有意思，我在1552之后专门刷了几道二分题，其中就有这一道，但是这一次依然没有很快的写出二分来。
首先我看到之后觉得应该用堆，是大顶堆还是小顶堆思考了很久，然后发现排序后，距离差有规律可循，所以就相当于
k路归并，于是实现了个小顶堆k路归并的版本，但是还是超时了，很惊讶。

看了下讨论，正确解法还是二分，首先二分策略一般是f(n) * log(n)这样一个复杂度，其中log(n)部分很夸张，基本
可以保证很小，10^9内仅仅就是30左右。只要能让f(n)复杂度足够低就可以，而根据这里距离差有序的这个规律，确实
可以把f(n)控制在O(n)，因此效率非常可观。

这里看来要强化一下对二分的认识，二分真的是非常非常快的。

另外再看一下堆的策略，首先堆也是一个很高效的结构，可以将问题降到log，这里是k，但是这道题有一个特点。f(k) * log(k)。 log(k)很小已经不用怀疑了，可是f(k)这一项，由于我们是求两两距离，长度为n的数组，计算两两距离
就变成了O(n^2)，复杂度一下子就上来了。 这一点确实没有想到。

一直在想log(k)相比log(n)带来的效率提升，却没想到k可以很大，大到n^2。
