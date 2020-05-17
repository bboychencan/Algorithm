# 1453

这一道题猛一看，似乎像是之前做过的，但再细看发现不是。 我尝试着遍历平面上所有的点，然后以
该点为圆心，计算此圆包含的点数，结果超时了。
然后感觉找不到思路，从来没有正式做过这一类的几何题，有点没有头绪，网上查了一下看看有一种
n^3的方法，然后看了下题目的数据大小，发现应该没问题。

思路很简单，任意找两个点，计算以r为半径，过这两点的圆弧，得到一个圆心。然后统计个数。

感觉思路很简单，但是计算圆心牵涉到浮点数计算有些麻烦，最后实现完有个case过不了。
结果看了别人的答案，才知道原来需要处理浮点计算导致的误差，需要加上一个很小的epsilon 1e-8 来
判断==的情况。

以后要适当练习一下计算几何类的题目。