# 1049. Last Stone Weight II

这一题，一个月内连续两次尝试都没有想出好的解决方案。
我的思路大概如下
1.脑子里没发找到一个最优子结构
2.隐约觉得先把最大的石头撞掉应该会是最优，像是贪心的方法，但是没有明确的思路去证明
3.用优先队列实现了一个2中描述的方法，结果出现测试错误
4.没有了思路。感觉石头之间的来回碰撞很难追踪，头脑中形成不了规律

看了答案后恍然大悟。
石头的撞击其实可以想象为多个石头合并成大石头再进行撞击，效果没有变化，取决于如何分组，只要到最后保证分出的两组差值最小即可，然后就可以转换成0-1背包问题。这一个想法非常令人震撼，不知道别人是怎么想出来的。

有人总结说，这一类撞击问题基本都可以用背包问题求解。

贴一下别人写的为什么可以用背包求解
Suppose you have rock a, b, c and d.

If you subtract them in the following order: b-c, then d-b-c. Then it is the same as doing d-(b+c).

Then doing [d-(b+c)]-a is the same as -a+d-(b+c), which is d-a-(b+c), which is d-[a+(b+c)], which is d-(a+b+c). (So doing things in that order will lead to this shortcut).
Lets try another order.

Suppose you have rock a, b, c and d.

If you do a-d, then b-c, then (a-d)-(b-c).

Then (a-d)-(b-c) is the same as a-d-b+c, which is the same as -d-b+a+c, which is -(d+b)+(a+c), which is (a+c)-(d+b). Another shortcut.
Then you can see that depending on the order of the subtractions, we get a different setting of difference between two groups.
