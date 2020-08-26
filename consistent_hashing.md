# Consistent Hash 一致性哈希

canssandra集群里面就用到了，主要作用是保证数据库访问可以均匀地分摊到不同的node节点，而且在节点增删变动的情况下一样能保持
一种均匀的分摊这个原则。

lintcode
- https://www.lintcode.com/problem/consistent-hashing/description?_from=ladder&&fromId=172
- https://www.lintcode.com/problem/consistent-hashing-ii/?_from=ladder&&fromId=172

## 普通hash的缺点
- 不方便扩展 普通的hash是采用链表数组来实现的，数组长度是固定的，但是如果一个节点被移除了，或者有新添加的节点，那么就需要
重新调整hash数组，可能所有的节点都要改变，成本很高。


## 原理
- 把所有的节点映射到2^64的一个集合上（环形，首尾相连），每个request同样被映射到2^64上一个点，然后从该点开始顺时针查找遇到
的地一个节点就是map的节点。
- 为了防止这些节点分布不够均匀，采用多次映射的方式，每个节点在2^64上生成m个节点，每个request遇到任何m个点中的任何一个都表
示映射到该节点。具体函数不记得，但是可以保证所有的点均匀的分布。
- 增加或删除节点的时候，把2^64环上该节点对应的m个点都删掉即可。