# 335. Self Crossing

这一题我花的时间有点久，主要是我整理的规律描述起来比较麻烦
发现有几个发现了更精简的规律

1.For each line, just check its next 6 lines. If not crossed, then skip it and do the same "6-line check" on the next line. Because if a line doesn't get crossed in 6 steps, then even if it get crossed later, some other line must get crossed before it.

还有一个类似的，把任意条线之后会不会交叉的情况列举了一下
situation1:fourth line cross first line;like a rectangle
situation2:fifth line meet first line;like a rectangle
situation3:sixth line cross first line;like a capital letter L{
x[i] represents the sixth line;
x[i-2]must bigger than x[i-4], or it won't cross or become situation 1,2;
x[i-1]must smaller than x[i-3], or it won't cross or become situation 1,2;
x[i-1]+x[i-5]must bigger than or equal to x[i-3],x[i]+x[i-4]must bigger than or equal to x[i-2] or it won't cross or become situation 1,2;
}

两个方法的思想是一样的，就是判断一条线在之后多少条线内有可能被交叉，否则再也不会。 这一个insight很重要，非常巧妙。很好的找到了这一规律。

一定要试图发现精简规律，当有思路但发现表述起来比较难的时候，就尝试着看看能不能找出更精简的规律来
