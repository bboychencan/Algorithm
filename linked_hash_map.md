# Linked Hash Map 

https://www.jianshu.com/p/8f4f58b4b8ab

这个概念也是新听说，有时间需要再学习一下

## 2020/08/08 学习一下 LRU， hashmap, hashtable, linked hash map， TreeMap 之间的关系

自己实现了一下LRU，还是很繁琐的。主要是节点更新的各种边界情况，如果是双向链表，每次移动需要更新6个指向关系。
同时为了更好的做操作，要存储dummy和tail节点。


尝试了一下用单链表实现，也是可行的，不过这里面更为tricky，需要在map中存储key值对应节点的前继节点。同时由于在删除节点后
仍然要能方便查询删除节点相邻的前缀节点，因此这里面新的节点应该放在tail，这样可以保证一直能拿到前继，如果放在链表头就不可以


最后也用linkedhashmap实现了一下LRU，对这几个树的区别也比较了解了。
- hashmap 是用一个数组加链表存储
- hashtable 好像是在多线程的情况下会好用一些，没有深入研究
- linkedhashmap 感觉就是专门为LRU设计的，实现就是一个hashmap + 一个双向链表，可以设定capacity，以及是否删除最老节点
  默认排序方法是插入的顺序，也可以设置为访问顺序遍历，这样就基本等同于LRU了。
- treemap 是用平衡树实现的有序map，遍历顺序可以保证是按照值的大小排序的。同时因为是树结构，插入更新都是O(logN)