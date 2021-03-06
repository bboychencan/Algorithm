# 区间问题
这类题目有很多种变种，解决方法有些不同，有很多时候是直接用贪心法，贪心算法一般比较难想到，而且比较难证明。

我之前在leetcode上做过一些这方面的题，感觉都是medium类型，没觉得很难，可是在面PonyAI的时候，一道区间的问题直接把我打趴下，第一轮都没过就gg了，我当时努力反思这道题为什么做不出来，总觉得区间的问题我从来没当回事过，是我的脑子不好使了？还是之前的题目做的太久已经忘了？ 我这里试图把这一类题目整理清楚，以后遇到同类的题目不至于再手足无措。


首先Pony的题目是要求一个被n个intervals共同覆盖的最长的区间，这个区间不一定是n个区间其中的某个。

这一个题目猛一看觉得很简单，立刻就先排序，然后依次从左往右，试图剥离问题。 可是这时候发现问题很难剥离出来，它是要求被最多区间所覆盖的那个区间长度。 这个问题似乎见过又似乎没见过。 他是一个变种。 
排序后我尝试依次比较交集区间，可是发现问题很难捋清楚，我总觉得这里面是用到堆或者单调队列，可是想了半天没有思路。 
最后被面试官提示用暴力解法先做，我发现暴力解法都不容易。。。 跟我想的不太一样。。。 最后跪地结结实实。


后来网上一查，果然完全一样的题没有出现过，但是类似的题我是绝对见过的，就是取一个点，使得该点被最多的区间所覆盖。
这个问题感觉容易想一些，可是题目要求求出那个区间，我就始终围绕这区间来思考，不肯把前后相交的区间给扔掉，结果把自己绕死了。


后来看了如果求一个点被最多区间覆盖，发现这个问题很简单，10行代码就能搞定，就是每个区间左右点放在一起排序，遇到开始点count + 1,遇到结束点count - 1, 这个思路不得不说非常巧妙，我一度怀疑我到底之前是否知道这个思路，如果不知道也就罢了，这次学到了。
如果以前曾经是知道这个思路的，那么我就很恐惧了， 为什么这么简单的思路，不到一年的时间现在完完全全想不到了呢？？ 


我开始觉得，我不应该再花过多时间去学习新的复杂的数据结构，我应该同时把以前做过的所有题都保证会做，且能秒做。 否则曾经做过的题拿来仍然是一脸蒙比，那岂不是之前的练习都白练了吗。


# 模板
Here I provide a concise template that I summarize for the so-called "Overlapping Interval Problem", e.g. Minimum Number of Arrows to Burst Balloons, and Non-overlapping Intervals etc. I found these problems share some similarities on their solutions.

Sort intervals/pairs in increasing order of the start position.
Scan the sorted intervals, and maintain an "active set" for overlapping intervals. At most times, we do not need to use an explicit set to store them. Instead, we just need to maintain several key parameters, e.g. the number of overlapping intervals (count), the minimum ending point among all overlapping intervals (minEnd).
If the interval that we are currently checking overlaps with the active set, which can be characterized by cur.start > minEnd, we need to renew those key parameters or change some states.
If the current interval does not overlap with the active set, we just drop current active set, record some parameters, and create a new active set that contains the current interval.

```
int count = 0; // Global parameters that are useful for results.
int minEnd = INT_MAX; // Key parameters characterizing the "active set" for overlapping intervals, e.g. the minimum ending point among all overlapping intervals.
sort(points.begin(), points.end()); // Sorting the intervals/pairs in ascending order of its starting point
for each interval {
      if(interval.start > minEnd) { // If the 
	 // changing some states, record some information, and start a new active set. 
	count++;
	minEnd = p.second;
      }
     else {
	// renew key parameters of the active set
	minEnd = min(minEnd, p.second);
      } 
 }
return the result recorded in or calculated from the global information;
```

## 以后刷提侧重
- 不做简单题
- 只做高点赞题目
- 拿到题5分钟内就有思路的题目不做
- 做过的题目也要再看一遍，有其实5分钟内没有明确思路的题目，一定要再多次练习，思考为什么没想出来。
- 追求最优解，以前做题追求数目，题目一AC就立刻忘掉不愿意再看了，应该没道题都写出最优解，同时思考多种思路


## 区间最大覆盖

## 无重叠区间最多个数
1520. Maximum Number of Non-Overlapping Substrings
这一题看完立刻知道要转换成无重叠区间最多个数的题目。 然后用贪心的方法去依次判断是否留下当前区间。
可是这一题一开始的区间构造花了半天的时间没想清楚，而且这是一道medium题，一下把我信心打击完。

后来看了结果，发现AC的也就100多人，心里平衡了一点，觉得自己智商还是正常。 
不过发现discuss的答案竟然和我的思路基本完全一样，我最后没写出来感到很遗憾。 今天的状态也不是很好。
中间变量命名也过于随意，导致后来修改的时候不断出bug

## 重叠区间个数

## 区间最大重叠度

## 不重叠区间最大数