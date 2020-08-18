# Presum

使用前缀和来减少计算区间和的时间，是在处理区间和问题的时候比较常用的技巧，但是有的时候是否使用presum比较隐晦，这个时候比较
考验水平。

## 简单型题目
一般题目需要频繁求区间和，很容易联想到presum

## 高阶
一次周赛遇到的题目
- https://leetcode.com/contest/weekly-contest-201/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
这个题目里不是简单的顺序使用presum，而是把presum的结果存储为map，当需要指定值的区间和时去map中查找，这个用法很巧妙