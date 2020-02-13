# 798 Smallest rotation with highest score

 Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point. 

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

## Note
这道题第一反应就是一个O(n^2)的解，不过显然TLE
琢磨了一会儿，感觉应该是每次移动，所有数值会改变1，但是没有继续深想，没有想出清楚的方法。
然后就看了高票答案。 
高票答案猛一看一头雾水，用了一个change数组，其中有几个地方思路跳跃，跟不上，看得很困惑。然后发现大家的反应都一样。
接着连着点了几个答案，发现有人提到用最大交集的interval的思路，突然一下子好像有灵感了，每个元素都有一个可以接受的移动K值区间，在这个区间内可以保证不减分，那么如果把所有元素的这个区间求一个最优的交集，那么就可以尽可能少的减少-1的发生。 大概思路是这样。
然后回头再看高票答案，发现还是有些搞不明白，那个change数组的含义，包括为什么change数组要累加。
琢磨了半天突然恍然大悟。原来这个解法有这几个知识点需要知道。
1. 每rotate一次，数组的score一定会加1， 因为第一个值移动到了最后（如果第一个值是0呢，特殊情况等会讨论），所有在i=0的值都肯定是0分的，但挪到最后之后一定会+1分。
2. 每rotate一次，最多有一个元素可以+1，那就是i=0的元素，其他元素均会左移动，导致坐标减小，一定不会比移动前的情况更好。
3. 只需要记录每移动一次，由零变一的元素个数即可。这样每移动一次，就知道数组的score减少多少，同时再加上默认的1
4. 如此一来，只需要记录每个元素减一发生时的k值即可。可以忽略本身就为负值，需要先加一再减一的情况，这种情况会被每次rotate默认加一给覆盖
5. 这样的话，change存储的就是每个k值会带来的-1的个数。
6. 从k=1开始，数组+1，并减去change[1]的值，再移动1时，数组再+1再减去change[2]的值，一次类推。
7. 最后返回change最大值的坐标即可。
8. 同时为了计算简便，直接把change初始化为1，这样就省去了每移动一次加一的操作。

总结一下，这里面有几个思维跳跃的地方，稍微不注意可能很困惑。