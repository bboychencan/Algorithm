# Ordereddict in Python
这个结构经常遇到，但自己没有用到过。 知道他跟Java的LinkedHashSet很相似。
都是一个有序的dict，除了在O(1)时间查询，修改，删除外，还能够按插入顺序进行遍历。原因都是因为底层采用了双向链表的结构。

直到做了460. LFU Cache的题目，决定自己使用一下这个数据结构