# Treemap

https://www.liaoxuefeng.com/wiki/1252599548343744/1265117109276544
https://zhuanlan.zhihu.com/p/44882350
https://www.jianshu.com/p/2dcff3634326

这个概念坑到了我，一直在用python刷题，python里面没有这个概念，结果后来才知道这是java自带的数据结构，底层是用了红黑树的实现，吐血。。。

感觉刷题以后还是要试着用java或c++，这样的话对底层的数据结构和时间复杂度有更清晰地认识，python撸的是挺爽，可是一些底层的结构都给封装起来了，list的append，[:i] + [i:]的操作具体的时间复杂度不是很清楚，dict用起来很爽，也没有太理解底层的实现。 这样不太好。。。


## Consistent Hashing 2020/08/05
在学习系统设计的时候，接触到一致性哈希，然后发现这里面非常适用这种结构。
于是用java的treemap实现了一下一致性哈希