# Longest Common Subsequence (LCS)

## Material
https://zhuanlan.zhihu.com/p/62521862

718. Maximum Length of Repeated Subarray
貌似一直没有针对练过这个最长公共子串和子序列的问题，总觉得更最长递增是同样道理，可是今天做这一题的时候竟然卡壳了，不知道是不是状态不好，反正只想出来了O(n3)的方法。 思路一直卡着，把dp[i]当公共子串的第一个元素，结果怎么想都觉要比对后面所有元素直到有不同。 

结果看了discussion才发现原来这一类dp应该是存储公共子串末尾元素。只是转一个小弯，一下子没转过来。
也没有更多往深入去想，导致这个本该很简单的题目没做出来，记下来作为教训。