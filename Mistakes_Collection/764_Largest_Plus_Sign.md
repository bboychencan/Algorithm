# 764. Largest Plus Sign


Medium
32069FavoriteShare
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.
An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

这道题，第一反应是做过类似的，但是用的就是普通的暴力解法，遍历整个grid，以每个点为中心扩散到最大记录下order。
也可能是状态一般，没有特别想要去寻找最优解。
稍微想了一下不知道有什么改进的方法。音乐想到了dp，但是没深挖。
把关注点放在了题目没有直接给matrix而是给了mines的list这一点，试图尝试从mines规模较小这一点找突破点。

看了答案，才想到原来可以dp。
思路很容易理解，主要考虑是每次扩展点的时候，确实有很多的重复判定，判定某个位置是否是mine，这个我自己也隐约想到了这一点，但是由于看题目是medium，有点低估了题目难度，没有往深入去想。 有点轻敌了。尤其是其他几道题感觉比较简单，甚至包括最后的hard题
