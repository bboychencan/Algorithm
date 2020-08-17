# Binary Search


## 2020/08/16
二分查找很好用，可以将O(n)的复杂度降到O(log(n))，使用二分一般是在单调有序的场景下。
如何能够识别出问题的单调有序属性是使用二分法的关键。 以前总觉得这类问题很简单，没有专门整理，可是这次周赛又挂在第三道medium
题上了，我本来尝试用dp，但是总是TLE。 
https://leetcode.com/problems/magnetic-force-between-two-balls/

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

## 进阶版（这个是我2020/08/16周赛跪的地方）
有些问题不是很冥想，第一眼很难想到用二分去求解。more often are the situations where the search space and search target are not so readily available. we might just turn to dynamic programming or DFS and get stuck for a very long time.

这个时候怎么知道可以用二分，As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- https://leetcode.com/problems/split-array-largest-sum/ （这题之前试过，总是TLE，放弃了。。。）