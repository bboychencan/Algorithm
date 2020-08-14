# R-tree

在空间信息的存储中常用的数据结构。Antonin Guttman 1984年提出。 
在LBS服务中很容易考察到。

R树的R是指Rectangle（矩形），R树是指满足以下要求的多叉树：

- 平衡树；
- 除叶子节点外每个节点都是一个矩形；
- 每个节点是它所有子节点的最小外接矩形；

R树和B树类似，在添加/删除节点时需要调整整个树的结构以保持平衡性，另外，R树还要调整被修改节点的所有父节点的大小，保证每个节点使它所有子节点的最小外接矩形，但是R树的查找效率很高。


综上，R树适合位置固定，*节点很少变化的地理元素*的空间索引构建。

# 跟geohash对比
geohash只擅长做点与点的距离计算，如果涉及到点，线，面之间的距离计算就不太行。 而R树可以处理任何不规则形状的空间信息，因为R
树会把所有的点线面都转换为矩形节点


Some of the advantages of geohash (comparing to r-tree) could be:

- easy implementation
- no performance degradation with growing number of features
- proximity searches (partially true)

Some of the disadvantages of geohash (comparing to r-tree) could be:
- arbitrary precision of grid
- harder to index (and query) line and polygon features
- size of the index could be large with some methods of line and polygon indexing
- by the specifications, it can be only used with longitude/latitude coordinate system, although the same method could be applied to other coordinate systems also