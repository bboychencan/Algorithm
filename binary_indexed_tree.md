# Binary Indexed Tree

## Source
https://oi-wiki.org/ds/bit/
https://blog.csdn.net/Jasmineaha/article/details/81462020

https://blog.csdn.net/Yaokai_AssultMaster/article/details/79492190
## Notes
需要再继续练习

## 一些技巧
刚学完BIT，把两道线段树的题目307 Range Sum Query - Mutable， 和 308 Range Sum Query 2D - Mutable
两道题用BIT的方法重做了一遍。本来以为BIT， segment tree的功能也就这样了，基本掌握了。

可是做了315 Count of Smaller Numbers After Self， 和 327 Count of Range Sum 才发现，原来BIT还有别的用法。
就是动态更新BIT，用来统计数据，非常的聪明。

现在简单总结一下我学到的BIT和segment tree的用法，特点
1. BIT适用于range sum query, 或者动态更新来做range count query. 但是处理range minimum/maxmium query比较困难。
2. Segment Tree比较全面，range sum， range min/max都可以，另外也可以做range count，range sum，或者其他。
3. 这两个结构都可以动态的生成和动态的查询。307，308这两道题都是要preprocess，把tree生成好，然后再做update和查询，这属于比较直白的range sum问题
4. 但是从315和327学到，BIT维护的数组不一定是原数组，也可以是重新构造的数组，这个时候需要把原问题做变换。如果只是原数组的range sum或者range min
未免过于简单。把问题进行变化就可以转换成BIT的结构，这里面的转换就是对关心的数值计算后并进行排序，然后逐步迭代，构建BIT，BIT数组存储的值是满足某种条件的
元素个数，这样BIT返回的前缀值即为满足某种条件的个数的总和。 这里如何把问题转换非常的关键。