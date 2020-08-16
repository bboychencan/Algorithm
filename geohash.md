# Geo hash 


映射到Base32，公共前缀越长，两个点越近。

原理比较容易理解，将地球表面划分到32个相等区域，然后再一次将每个区域再进行一次32划分

因为映射到了一维，所以可以利用数据库的功能。
而R树大多需要在内存中使用，无法利用数据库的功能。

lintcode geohash

## 数据库中geohash range 查询
数据库，字符串前缀匹配，例如
- SQL， LIKE '9q9hv%'
- NoSQL, Cassandra, 将geohash设为column key，使用range query(9q9hv0, 9q9hvz)
- NoSQL, Redis, Driver 位置 存储在 三个key 9q9hvt, 9q9hv, 9q9h 中， 每个key里面维护一个drivers set


# Geo Fence

基于城市来划分