# Sqrt Decomposition
这个概念似乎不难理解，但是在算法中应用确实头一次碰到。
这个概念是出现在 ‘1265. Print Immutable Linked List in Reverse‘ 这道题上。
follow up中文是否可以把空间复杂度缩减到
1. Constant space complexity?
2. Linear time complexity and less than linear space complexity?

我可能理解错了，以为是要找到一个方法满足这两个要求，其实是要求分别找到两种方法满足以上两种要求。
这样的话似乎没那么难，对于第一项需要n^2的方法。 对于第二项，只是要求'less than linear space complexity'其实
从这个描述就可以看出，并没有要求达到constant的space，这时候可以考虑sqrt decomposition的方法，算是一个小技巧。