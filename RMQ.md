# RMQ Range minimum query

Segment tree is a standard solution for this problem, besides, there is sparse-table and BIT.

## ST
2020/06/15

在做周赛1483 Kth Ancestor of a Tree Node这一题的时候，提交了几次都是TLE，当时不知道问题在哪。
后来看了别人的答案才知道这种求解LCA有专门的解法，里面一个很重要的思想是倍增, binary lifting。 ST就是利用了这个思想的一种数据结构

简单来说，就是区间dp，但是如果把所有的区间存下来可能空间太大。 所以用一种二进制压缩的方法把第二维压缩到logn，然后在
查询的时候利用区间最值的特性，可以在O(1)的时间内查询到，但是ST有个缺点就是不支持修改，这样保证了可以在O(1)时间查询。 如果需要支持修改可以用BIT

```python

def preprocess():

```

