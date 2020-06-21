# RMQ Range minimum query

Segment tree is a standard solution for this problem, besides, there is sparse-table and BIT.

## ST
2020/06/15

在做周赛1483 Kth Ancestor of a Tree Node这一题的时候，提交了几次都是TLE，当时不知道问题在哪。
后来看了别人的答案才知道这种求解LCA有专门的解法，里面一个很重要的思想是倍增, binary lifting。 ST就是利用了这个思想的一种数据结构

简单来说，就是区间dp，但是如果把所有的区间存下来可能空间太大。 所以用一种二进制压缩的方法把第二维压缩到logn，然后在
查询的时候利用区间最值的特性，可以在O(1)的时间内查询到，但是ST有个缺点就是不支持修改，这样保证了可以在O(1)时间查询。 如果需要支持修改可以用BIT


## Example of Range Minimum Query
```python
def buildSparseTable(arr, n):
    # Initialize M for intervals with length 1
    lookup = 
    for i in range(n):
        lookup[i][0] = arr[0]

    j = 1

    while (1 << j) <= n:
        # compute minimum value for all intervals with size 2^j
        i = 0
        while (i + (1 << j) - 1) < n:
            if (lookup[i][j-1] < lookup[i + (1 << (j - 1))][j - 1]):
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
            i += 1

        j += 1

def query(L, R):
    # Find highest power of 2 that is smaller  
    # than or equal to count of elements in  
    # given range. For [2, 10], j = 3  
    j = int(math.log2(R - L + 1))  
  
    # Compute minimum of last 2^j elements  
    # with first 2^j elements in range.  
    # For [2, 10], we compare arr[lookup[0][3]]  
    # and arr[lookup[3][3]],  
    if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:  
        return lookup[L][j]  
  
    else: 
        return lookup[R - (1 << j) + 1][j]  

```

