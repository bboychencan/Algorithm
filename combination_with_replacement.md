# Combinations with replacement

今天随意参加了一下Atcoder，a，b两题无脑简单，到了c题的时候，一下子有点慌了。猛一看，约束条件这么多，元素之间的corner case又那么多，都是小于或等于的关系， inclusive。 感觉光是判断这些corner case就要蒙了。 可是一想，这才第三题，前两题又是无脑。这是怎么搞的，难道是太晚了脑子已经有点晕了吗？

仔细再一看，发现限制条件里N和M的值都很小，只有10，心想这个应该直接遍历所有方式进行判断即可。 可是一下子又有点慌了，我开始
尝试想从N个元素选出递增的M个有多少种方法，关键看到这些相邻元素是可以相等的，我先是把他当做permutation来看，这样的话有10的10次方，突然觉得可能不妙。 然后就想怎么把这所有的permutation转成组合，可是突然觉得这个似乎不是很容易。 然后就在想这道题到底是不是简单题？ 难道从a,b到c跨度这么大吗。

然后我开始想别的思路，发现dfs应该是可以的，但是一想这里面边界条件应该也不少，心里觉得不甘心，不想为这么个简单题写这么复杂的解法。然后又想了一会儿始终
没找到思路。


看完答案之后，才发现，原来是自己排列组合的知识有漏洞。 N个元素里可重复地取M个元素复杂度并没有很恐怖。 至于为什么没有能够有这个直觉，是因为这里面考察
了一个“重复组合”的概念。 在排列组合里，重复组合是一个比较特别的情况，Cr(N, M) 其实等于 C(N+M-1,M)可见并没有很大。

这个小小的知识点，我没有印象，结果导致了这道题迟迟没有思路，，，， 真是，，，， 

同时itertools里面还有combination_with_replacement这个方法，因此直接拿来使用，代码非常简短。。。 


果然，又加深了这个观念，当觉得迟迟没有思路的时候，很可能是知识点有漏洞。短时间内想出从没有见过的解法不太现实。