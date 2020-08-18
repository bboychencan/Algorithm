# Collection of failed problems

- 128 Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/
```
这一道题用nlogn的方法很快写出了解，但是仔细看了下题目要求O(n)，然后转为以数字为坐标的数组，
但是内存溢出。想了并查集，发现明显变复杂了。然后就没有思路了。。。
看了答案，大家都用了Hashset，反思一下自己对Hashset的性质不够熟悉，总觉得set的使用牵扯到查
会带来logn的复杂度，但其实set的操作都是O(1)的，查询只需要O(1)，只需要O(1)！只需要O(1)！
需要O(1)！
下次一定记住了！

以后当题目要求时间复杂度在O(n)以内时，记得想到Hashset
```

- 240 Search a 2D Matrix II https://leetcode.com/problems/search-a-2d-matrix-ii/

```
2020/02
这次春节假期一下子隔了接近一个月没有刷题了，现在手非常的生疏，很多难度不高的题都需要花很长时间
，脑子没有那么清晰了。感觉很慌，生怕之前花的那么多时间和精力都白废掉了。

按分类刷题的时候遇到了这一类题，找第k个指，在排序的一维或二维数组上。 这道题之前做过，类似的
题也做过好几道。可是时隔很久如今再重新做起来的时候，感觉非常的吃力。总记得是有一个小技巧在排序
的2维矩阵中找到target值，但是一直捋不清楚这个思路，非常的慌张最后看了一下讲解，内容确实是记
得的，也理解了思路，并没有很难，可是在自己做的时候无论如何也想不到那一步。 

这让我觉得很恐慌，首先我之前花了那么多时间把这些技巧灌进脑子里，可是只是短短几个月的功夫，全部
忘得一干二净。 另外让我想到了刘未鹏书里写到的，他当时研究哈夫曼编码的时候的情形，他看完哈夫曼
编码的思想后觉得非常简单，自己怎么能想不到呢，可是隔了一段时间自己试图重新自己推出哈夫曼编码时
，屡屡受挫，他说那些数学定理看起来都非常的浅显易懂，可是自己如果尝试从头推导的话会非常的难这两
者的思考方式不同。要学会那种解数学问题的思考方式，类比以往的经历，简化问题等等。
```

- 309 best time to buy and sell stock with cooldown https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

```
2020/05/13
这一题四年前做不出来， 一直没有思路。
2020/05/13 再看这道题目的时候，很快有了思路，应该就用dp，只是dp的转移方程稍微需要思考一下。
```

- 312 Burst Balloons (hard) https://leetcode.com/problems/burst-balloons/

```
2020/02/01
这道题看完后觉得第一反应是用递归的dp，把整个数组序列作为key存到dp中，这样来减少重复计算，可
是一想这个key长度会很大，感觉肯定不是最有办法。然后就没有思路了，想了几分钟感觉不知道如何找到
更优的解，所以就放弃了。

看了一下答案，发现这里的核心在于找到转移方程，其实dp的问题关键就在于找到转移方程。
这里面的思路，不是把整个数组都存作key，而是把区间起始结束的index作为key。
这里面可以简化的一个很重要也很巧妙的点就是，当爆破一个i点的气球后，左边和右边的数组会有一个转
移方程。
1. 如果是以先爆破的气球来去做状态转移的边界的话，那么就很难以此起球的坐标把数组分割成左右两部
进行状态转移，因为两个数组的边界会有交集，并非完全独立。
2. 这里面有人提出了一个非常巧妙的分割方法，**以最后一个爆破的气球**作为状态分割点，这样的话
就可以保证左右两边的数组互不干涉。核心就在找到这个一个状态转移的规律！
dp[i][j] = max(dp[i][k] + dp[k][j] + nums[k] * nums[k-1] * nums[k + 1]) (k in 
n)
3. 当遇到需要把整个区间存入dp做key时，先考虑一下是否有方法只存区间的起始和末尾值。
4. 一般这种dp有两种方法，bottom-up和top-down，bottom-up就是从最简单情况计算，然后逐步用
循环计算复杂情况。而top-down采用递归的方法直接从复杂情况计算，在过程中存储中间结果防止重复计
算。
5. 还有一点关键的地方就是处理边界情况。
```

```
2020/05/10
## Updates on 2020/05/10
今天尝试做题目546. Remove Boxes时，看到discussion里面有人提到312和546是类似的题目，就转
过来回看312之前的笔记，发现这一道题当时也是没有思路，只想着说把所有数组序列存入做key运用dp，
但是很明显行不通，然后就没有思路了。

今天过了这么久回看，发现这道题还是没有思路。。。 之前看别人答案总结的头头是道，但是现在过了两
个多月回看，一丁点印象没有，而且别人的思路还是无论如何也想不到。。。

```

- 316 remove duplicate letters  https://leetcode.com/problems/remove-duplicate-letters/

```
2020/05/13
这道题4年前和2个月前都尝试过，但都失败了，2020/05/13 再次回看这道题的时候，很快就有了思路，
这应该使用单调队列来存储之前的最长单调序列。只是这里的情况稍微有些复杂，需要判断的情况稍微复杂
点，多花了点时间
```

- 327 Count of Range Sum https://leetcode.com/problems/count-of-range-sum/

```
2020/04/28
这一道题，猛一看不难，很快就有了O(n^2)的思路，但是很明显，这个方法会超时。
然后开始仔细研究其中的规律，看看是否可以利用two pointers来优化这个搜索过程。
想来想去，尝试了建立max、min数组，存储以当前坐标开头的所有数组的最大和和最小和，这个方法虽然
可以减少一些判断，但整体上还是O(n^2)的。然后又尝试了修改为背包问题，这样就变成了带有负值的背
包问题，这个问题没有经验，尝试着写了一下，结果WA。
然后就实在没有头绪了，总觉得应该是用two pointers，可是找不到two pointers的规律。
看了下答案，有不少人提到two pointers，但是two pointers的前提是数组的单调性,看了几个不错的
答案，发现这道题是到难题，没有想出来并非是卡壳，而确实是因为这道题比较复杂，比较好的解法有
1.线段树
2.merge sort
正好用这个机会学习一下线段树算法
```

- 335 Self Crossing https://leetcode.com/problems/self-crossing/submissions/

```
2019/10/10
这一题我花的时间有点久，主要是我整理的规律描述起来比较麻烦
发现有几个发现了更精简的规律

1.For each line, just check its next 6 lines. If not crossed, then skip it and
 do the same "6-line check" on the next line. Because if a line doesn't get 
 crossed in 6 steps, then even if it get crossed later, some other line must 
 get crossed before it.

还有一个类似的，把任意条线之后会不会交叉的情况列举了一下
situation1:fourth line cross first line;like a rectangle
situation2:fifth line meet first line;like a rectangle
situation3:sixth line cross first line;like a capital letter L{
x[i] represents the sixth line;
x[i-2]must bigger than x[i-4], or it won't cross or become situation 1,2;
x[i-1]must smaller than x[i-3], or it won't cross or become situation 1,2;
x[i-1]+x[i-5]must bigger than or equal to x[i-3],x[i]+x[i-4]must bigger than or equal to x[i-2] or it won't cross or become situation 1,2;
}

两个方法的思想是一样的，就是判断一条线在之后多少条线内有可能被交叉，否则再也不会。这一个insig
ht很重要，非常巧妙。很好的找到了这一规律。

一定要试图发现精简规律，当有思路但发现表述起来比较难的时候，就尝试着看看能不能找出更精简的规律
来
```

- 336 palindrome pairs https://leetcode.com/problems/palindrome-pairs/

```
2020/05/13
这道题3个月前和6个月前都尝试过，失败了。 2020/05/13 又尝试了一下，发现不难，只要用hashmap
存储一下某些前缀即可，写完后稍微调试了一下就AC了，感觉这段时间还是有进步的看来。
```

-  373 find k pairs with smallest sums https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

```
2020/05/08
I have tried solving this problem 7 months ago using a brute force way ......
 and it worked ......
(I learned a lesson, brute force does help me with learning algorithm at all)
I don't know for what reason, I retried this problem 3 months ago, and the 
solutin looks very legit, same as the top voted 
solution. I'm not sure did I come up with that all on my own or just just 
 borrow the top voted solution. 

And, on 2020/05/03, in the weekly contest, I confronted a similar problem and 
 tried my best, just can't figure out the solution.

After checking the discussion, I found it's a variant based on this 373 
problem, which made me feel very frustrated... 
I don't know why I can't find the solution although I obvisously had solved it
 before. 

I think there are several reasons.
1. I'm not in best condition this week ... (Yes, it's true, highly possibly,
 becasue I did not eat well, I cook for myself since this week,
and mainly Chinese food, with very heavy oil ... and I feel dizzy throughout 
 the whole day, and did't notice that until now. I feel more lazy 
and sleepy than before, I don't want to think about difficut problems and not 
feel excited when facing chanllenging problems, not like before.
and I did not sleep well too, I went to bed very late, thanks to the WFH. So I
 decided to change from today, I will make salad as meal at least
once a day, and I will go to bed on time, let's check out if this helps.)

2. I did not solve 373 on my own last time, maybe I tried, but had no clue,
 and simply looked at the discussion and implemented it ......
This idea is a little tricky, it converts the problem into finding k-th value
 in Young-table, and the solution becomes obvious.

3. The variant in 2020/05/03 weekly contest is more complex, you need to apply
 the finding k-th value in Young-table multiple times.
```

- 381 Insert Delete GetRandom O(1) - Duplicates allowed https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

```
2020/05/13
这一题考察对底层数据结构的了解。

2年前尝试过这道题，没解出来，现在2020/05/13重新看这道题的时候，很快想到用python里面的
counter去存储每个元素的频率。至于说随机抽样，查了一下，python里面有random.choices with
weights，即可以根据weights来进行抽样。可是这里面有一个问题，random.choices只能对支持
indexing的结构操作。而set本身不支持这个。我第一反应就是直接把set转成list不就行了嘛，一行代
码的事。可是忘了考虑这个操作是需要O(n)的。虽然代码写起来很快，但是其实效率不高，面试的时候很
可能会被挂在这。

后来看了下别人的解，才发现一个非常巧妙的方法，那就是用一个dict来存储每个元素所在的所有index 
，另外一个数组来存储所有元素。
数组可以用来抽样，插入操作只需要把元素append到数组末尾，而remove操作就很巧妙了，通过记录的
val在dict中的index值，交换数组index处和数组末尾处的值，然后把nums数组删除最后一位即可。
这个方法非常地聪明，值得学习。
```

- 445 Add Two Numbers II https://leetcode.com/problems/add-two-numbers-ii/submissions/

```
2020/02/11
这一个题一看不难，有了第一想法就开始写，先计算两个链的长度，取较长的作为基准，然后相加等等。
写着写着发现一些判断条件比较多，变得有些繁琐和不耐烦
看了下高票答案，发现用stack的话问题就变得清晰很多。 这种题竟然没想到用stack做一下。
```

- 478 generate random point in a circle https://leetcode.com/problems/generate-random-point-in-a-circle/

```
2020/05/10
This problem type is quite rare and interesting, it's a probability problem. 
I quickly got the idea to use the polar coordinate to generate random R and 
random degree, however the answer is incorrect, I can't debug this since it's 
a probability problem.
After checking the discussion, I did estimate the probability carefully 
enough. Simply generate random R is not correct, given the area size is Pi * 
R^2, and we want to make the probability propotional to the size of the area, 
which, for instance, when Pi = 1, the area size is Pi, when Pi = 2, the area 
size is Pi * 4, and to make the probability propotional, the sqrt of R should 
follow uniform distribution.
```

- 525 Contiguous Array https://leetcode.com/problems/contiguous-array/

```
2019/11/26
这一天一个月内先后尝试了两次，都失败了，看了答案之后发现本身并没有很难，只是用到了一个小的
trick我从来没有遇到过。
看到题目后第一反应是，这道题很像two pointers或者sliding window的题目，我开始琢磨通过移动
前后两个指针或者从start和end开始把数组向内压缩，试图找到压缩过程中的规律从而可以把对数组的遍
历从n^2次降低到n次。
这种尝试花费了我将近一个小时，似乎能够捋出一点规律，但是很容易就被一些corner case的fail了。
我还试图用dp，先计算presum，从两个方向进攻，依然没有头绪，因为遇到0或者1之后下一步该如果操作
很难判断，或者说没有明确的规律。

翻看答案后，发现有一条很重要的思想我没有想到过，那就是把曾经出现过的presum用hashmap存储下来
，这样同样的presum值再次出现后就意味着，新添加的一段数组中0和数目相同。

数组中0和1的个数相同这件事情，可以通过把0转化为-1，然后求和为0得到简化，这一点很巧妙。不知道
为什么没有想到。 这样就把0和1数目相同这个问题变成了和为零的问题

```

- 546 remove boxes https://leetcode.com/problems/remove-boxes/
```
这一道题之前标记过，过了很久现在再看，猛一看依然是没有思路，虽然现在也练习了不少的数据结构，
但是这一道题迟迟找不到思路。开始有点担心，然后稍微翻了下discussion，发现大家都用的dp，我也
尝试过dp，但是一直分离不出来最优子结构。
这个让我有点担心，看来这个不是数据结构不熟悉的问题，而是对于dp还没有百分之百的把握。我想知道
到底什么原因没有能很快的有思路。
到底是因为思路不够发散，还是说dp的种类有很多，那些其他的种类都还没掌握，有一点点心虚，一定要
再一次巩固dp。
```

- 560 Subarray Sum Equals K https://leetcode.com/problems/subarray-sum-equals-k/

```
2019/10/15
这一道题，我2019/10/15做过，看了一下记录，发现当时知道了用map存储presum，不过貌似当时也是
看了答案才知道的。
因为我发现后来又做了一次提交，使用了扫描整个数组的笨方法，然后TLE。
但是2020/08/10 在做 1546. Maximum Number of Non-Overlapping Subarrays With Sum 
Equals Target 这道题的时候，我彻底懵逼了。 
当然里上一次做类似的题目很久确实有关系，但是也说明我没有掌握这个presum存储为map的方法。

所以我打算这次记录下来，让自己印象深刻一些，同时我希望以后不要急着冲数量，很多题看了下答案之后
知道怎么做了，但是可能并没有提取题目类型，以后遇到类似的题还是会做不出来。 
以后可以专注把以往做过的题回顾一遍，确保做过的题型都能够牢固的掌握。
```

- 1546 maximum number of non-overlapping subarrays with sum equals target https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

```
2020/08/10
2020/08/10 在做 1546. Maximum Number of Non-Overlapping Subarrays With Sum 
Equals Target 这道题的时候，我彻底懵逼了。 
发现560 很类似，之前做过，但是似乎之前也没有直接想出来最优解，可能也是看了答案才会做的，所以
并没有掌握这个题型。

以后要多回顾，多总结
```

- 764 Largest Plus Sign https://leetcode.com/problems/largest-plus-sign/

```
2019/11/09
这道题，第一反应是做过类似的，但是用的就是普通的暴力解法，遍历整个grid，以每个点为中心扩散到
最大记录下order。
也可能是状态一般，没有特别想要去寻找最优解。
稍微想了一下不知道有什么改进的方法。音乐想到了dp，但是没深挖。
把关注点放在了题目没有直接给matrix而是给了mines的list这一点，试图尝试从mines规模较小这一点
找突破点。
看了答案，才想到原来可以dp。
思路很容易理解，主要考虑是每次扩展点的时候，确实有很多的重复判定，判定某个位置是否是mine，这
个我自己也隐约想到了这一点，但是由于看题目是medium，有点低估了题目难度，没有往深入去想。 
有点轻敌了。尤其是其他几道题感觉比较简单，甚至包括最后的hard题

```

- 798 Smallest rotation with highest score https://leetcode.com/problems/smallest-rotation-with-highest-score/

```
2020/02/13
这道题第一反应就是一个O(n^2)的解，不过显然TLE
琢磨了一会儿，感觉应该是每次移动，所有数值会改变1，但是没有继续深想，没有想出清楚的方法。
然后就看了高票答案。 
高票答案猛一看一头雾水，用了一个change数组，其中有几个地方思路跳跃，跟不上，看得很困惑。然后
发现大家的反应都一样。
接着连着点了几个答案，发现有人提到用最大交集的interval的思路，突然一下子好像有灵感了，每个元
素都有一个可以接受的移动K值区间，在这个区间内可以保证不减分，那么如果把所有元素的这个区间求一
个最优的交集，那么就可以尽可能少的减少-1的发生。 大概思路是这样。
然后回头再看高票答案，发现还是有些搞不明白，那个change数组的含义，包括为什么change数组要累
加。
琢磨了半天突然恍然大悟。原来这个解法有这几个知识点需要知道。
1. 每rotate一次，数组的score一定会加1， 因为第一个值移动到了最后（如果第一个值是0呢，特殊情
况等会讨论），所有在i=0的值都肯定是0分的，但挪到最后之后一定会+1分。
2. 每rotate一次，最多有一个元素可以+1，那就是i=0的元素，其他元素均会左移动，导致坐标减小，
一定不会比移动前的情况更好。
3. 只需要记录每移动一次，由零变一的元素个数即可。这样每移动一次，就知道数组的score减少多少，
同时再加上默认的1
4. 如此一来，只需要记录每个元素减一发生时的k值即可。可以忽略本身就为负值，需要先加一再减一的
情况，这种情况会被每次rotate默认加一给覆盖
5. 这样的话，change存储的就是每个k值会带来的-1的个数。
6. 从k=1开始，数组+1，并减去change[1]的值，再移动1时，数组再+1再减去change[2]的值，一次
类推。
7. 最后返回change最大值的坐标即可。
8. 同时为了计算简便，直接把change初始化为1，这样就省去了每移动一次加一的操作。
总结一下，这里面有几个思维跳跃的地方，稍微不注意可能很困惑。
```

-  818 race car https://leetcode.com/problems/race-car/ 

```
2020/03/10
这道题猛一看似曾相似，大概是用二进制编码，然后求最优的变化序列。
但是仔细想了一会发现二进制的规律似乎在这里用不到。还是要用dp。
然后就开始写dp的方法。但是dp的方法有个问题，这里面的状态变化理论上来说有无穷种，如何去做
pruning，这个想了很久。
先定了几个假设：
1. 在超过target之前，汽车永远不需要掉头
2. 在超过target之后，汽车需要立刻掉头。
3. 在超过target之前，可以采用原地RR的操作将速度重新减为1，但方向不变。
基于这几个假设我写出来的答案，发现5，43这两个通不过。 苦思冥想找不到答案。
看了一下讨论发现这上面的假设有错误。正确的假设如下
1. 在超过target之前，汽车可以掉头，但只可能发生在离target最近的时候
2. 在超过target之后，汽车需要立刻掉头。
3. 在超过target之前，汽车掉头回跑的距离不会超过掉头前离target的距离
这几个假设不知道怎么证明，按这个方法写完确实AC

```

-  864 Shortest Path to Get All Keys https://leetcode.com/problems/shortest-path-to-get-all-keys/

```
2019/12/23
这一道题目虽然别人整理的分类是bfs，但是我看了一下之后觉得这不应该是dfs吗，只是加了key而已，
于是就写了个dfs的解，两个测试用例通过了，但是提交后还是wa，一看错误例子，才发现原来是需要回溯
，因为这里并没有假定走到某个点就不能往回了，而dfs在遍历的时候基本是不访问visited的点的。

看了一下discuss，发现大家都在用bfs，也有提到A*的，才发现这是一类我没有怎么练过的题。
因为考虑到会有回溯的情况，但是同样是一个位置，不同时间访问状态会有区别，也就是keyset会有差别
。因此只需要在visited的集合里多加一个keyset这个元素就行，这样就可以保证visited过的状态不需
要再重新访问。
```

- 943 Find the Shortest Superstring https://leetcode.com/problems/find-the-shortest-superstring/

```
2020/04/03
这一次的weekly前三道题我20分钟AC了，还在想这次的题有点简单。结果就在这一题上卡了1个小时没做
出来。
我面对这个题的时候发散了几个思路，最终还没想出答案，但是看了讨论之后发现我其中一条思路是正确的
，记录一下我的思维过程
1.第一反应是两两判断首尾是否有公共子串然后就可以合并了
2.但是当出现第三个字符串的时候，我一直无法判断前两个的合并是否正确，
3.我拿了好几个例子来实验，发现前两个确实不能用贪心来合并，很可能第三个更适合其中一个的首尾拼
接
4.我闪现出了一个通过连接图来记录每个字符串可达点的方法。但是在形成图之后我没有想法该怎么做。
5.我继续试图用我熟悉的动归来解决，一心想找出来最优子结构。可是发现似乎没有这个规律，前n-1想的
最优解始终找不到跟第n项之间的关系。我卡在了这里，写了好多个例子，试图找出规律，但是时间很快就
过去了。
6.我也想到了先进行排序，不过排序后发现似乎没有什么帮助，排序可以让有共同前缀的字符串聚在一起
，但是对拼接似乎没有作用。要做拼接需要的是首尾有共同序列。
7.看了讨论提示后，才发现高票答案用了连接图的方法，然后用traveling salesman求解最短路径。

总结一下：我的思维发散过程中，这次确实是找到了线索，但是没有深挖下去。原因是我对旅行商问题似乎
做的不多。 一想到图我脑子里反应出来的是深搜，dp。 
但是这一题当时那一瞬间我没有在脑子里建立起旅行商问题和这个题解的联系。

我想过说记录每个字符串可以首尾衔接的字符串的列表，但是下一步该怎么办我那一瞬间没有思路，所以就
放弃了。脑海里试图在脑中构建图的搜索过程，发现复杂度过高，没法直观的在脑子里模拟，所以放弃了。

当时想到构建了图，然后应该想到首尾遍历然后知道遍历所有结点，然后找到最小值。 
但是我当时可能有几个疑问，一个是怎么样保证这样一直首尾连接下去得到的是最优解。 另一个是当时想
到了固定某个跟的遍历，觉得固定这个根的遍历可能无法得到最优，需要从所有点都遍历下。 
当时脑子中试图模拟这个过程，发现复杂度太高，所以没有继续往下想了。

经验就是
1.首先对旅行商问题不够熟悉。
2.第二就是当把问题抽象为图问题之后，应该去想图的已有的问题和解法，而非试图在脑中模拟图的求解
过程，那样势必太难。应该联系到现有的解法。
3.或许一条思路如果超过5分钟没有明确方法的话，应该换条思路。每条思路又不能太短，如果只是脑子一
闪而过，很可能错失

这一题隔了一个月学习了旅行商问题，研究了别人的答案后，终于写出了AC，从理解这个解法到自己写出
AC花了将近8个小时，可以说是目前遇到的最难的问题了。

这一道题比较复杂，首先关于这个最优子结构，一开始有点卡壳，看了一些blog，总觉得哪里不对。后来
才发现很多blog写的最优子结构是针对已经固定出发点的情况，且在遍历完之后需要回到出发点。
而这一题虽然是旅行商问题，但是有一些变化
1. 没有说明出发点，需要考虑所有出发点的解，最后再求出最
2. 这里没有要求回到初始点，只需要遍历所有点即可。
3. 这里有一个path储存最优路径，这个在很多其他的blog上没有看到。 
这个path非常重要，非常smart
总结一下，旅行商问题可能会有很多变种，取决于出发点是否固定，是否要返回终点等，针对具体情况，需
要有所针对的变动。
尤其是很多边界条件需要谨慎。
以后问题不仅需要给出最优解的值还需要给出最优路径的时候，一定要想到用path去存储最优路径的上一
个结点，非常关键！
```

```
2020/04/03
## Update on 2020/04/03
时隔四个月再次遇到类似的题目，一时间没有思路，大概花费了1多分钟想到了这是一道旅行商问题，同时
意识到似乎有些压缩的操作，但是由于这类题目练的少，想不出具体的解法。
关键的是当时还不知道这类题目叫做状态压缩dp，在李煜东的书里有讲解过，这次算是打通了这个概念，
加深了状态压缩的思想，剩下的就是再熟练梳理出最优子结构和状态转移方程。
这次重新手写一遍，然后把答案记录一下。
```


- 956 Tallest Billboard https://leetcode.com/problems/tallest-billboard/

```
2019/11/21
这道题猛一看还以为不难，标准的背包问题，稍微仔细想了下，感觉有点麻烦，需要拼出两个一样的长度而
且有可能有剩余不用的rod，发现这个比较难捋清了。

不过还是写了个背包方法，dp[i]里面存储拼接长度为i是的所有拼接组合，然后每次遍历的时候都判断i/
2的所有组合情况，找出i和i/2里面没有共同元素的组合方式，然后就可以得到一个解。遍历完所有i，所
有解中最大值即为答案，结果TLE。。。

过了半个月回头再想这道题，还是没有更好的思路，唯一的就是把选取状态压缩到01的数字中，避免存储
一些列的set，感觉应该会降低时间复杂度。

看了答案，结果发现大家用了二维的数组去存背包状态，我试图往这个方向去想过，但是没有很明确的思路
，所以也放弃了。

隔了几天用状态压缩去实现了上面的想法，仍然是TLE。

看了一些答案，感觉很多把问题搞复杂了，其实还是不需要二维数组。这依然是一个背包问题，但是唯一的
变种就是，这不再是0-1背包问题，而是0，1or-1背包问题。每次判断的不光是加入或不加入当下元素，
而是判断是加，是减，或者忽略这三种情况，遍历所有三种情况，存储最优值即可。 
这可以算上背包的变形，第一次遇到，值得记住！～
```

- 979 distribute coins in binary tree https://leetcode.com/problems/distribute-coins-in-binary-tree/

```
2020/05/13
这一道题，很久之前尝试过一次，没有捋出思路，当时试图梳理出最优转换的细节，在何种情况下如何转移
可以实现最优。 可是发现情形有很多种，一种种对应的话会很复杂，最后就放弃了。

时隔这么久，今天重新看这一道medium题，第一反应就是应该尝试用recursion的思路去解决这个问题，
先从简单的case开始，如果只有一个root节点和一个left，一个right的时候该怎么判断。本来想着说先
把每个subtree的元素个数计算出来，然后减去subtree的node总数用来作为需要迁移的元素的总个数。
后来发现其实在递归的过程中on the fly计算也是可以的。然后慢慢思路就清楚了，写完答案自己也有点
惊讶一次就AC了。

```

- 1049 Last Stone Weight II https://leetcode.com/problems/last-stone-weight-ii/

```
2019/11/12
这一题，一个月内连续两次尝试都没有想出好的解决方案。
我的思路大概如下
1.脑子里没发找到一个最优子结构
2.隐约觉得先把最大的石头撞掉应该会是最优，像是贪心的方法，但是没有明确的思路去证明
3.用优先队列实现了一个2中描述的方法，结果出现测试错误
4.没有了思路。感觉石头之间的来回碰撞很难追踪，头脑中形成不了规律

看了答案后恍然大悟。
石头的撞击其实可以想象为多个石头合并成大石头再进行撞击，效果没有变化，取决于如何分组，只要到最
后保证分出的两组差值最小即可，然后就可以转换成0-1背包问题。这一个想法非常令人震撼，不知道别人
是怎么想出来的。
有人总结说，这一类撞击问题基本都可以用背包问题求解。

贴一下别人写的为什么可以用背包求解
Suppose you have rock a, b, c and d.

If you subtract them in the following order: b-c, then d-b-c. Then it is the same as doing d-(b+c).
Then doing [d-(b+c)]-a is the same as -a+d-(b+c), which is d-a-(b+c), which is d-[a+(b+c)], which is d-(a+b+c). (So doing things in that order will lead to this shortcut).
Lets try another order.

Suppose you have rock a, b, c and d.

If you do a-d, then b-c, then (a-d)-(b-c).

Then (a-d)-(b-c) is the same as a-d-b+c, which is the same as -d-b+a+c, which is -(d+b)+(a+c), which is (a+c)-(d+b). Another shortcut.
Then you can see that depending on the order of the subtractions, we get a different setting of difference between two groups.
```

- 1145 Binary Tree Coloring Game https://leetcode.com/problems/binary-tree-coloring-game/

```
2019/11/05
这一题AC了，花的时间半小时左右，不是很满意。

最开始看的时候有点紧张，担心要用到图的一些理论，比如联通路径，桥之类。简单记录一下我的思维过程
1.第一开始觉得需要求解桥
2.感觉是棋类博弈，开始有点担心这类题做得不多
3.仔细读题目，发现二叉树里面任何点都是桥，因此松了口气。
4.然后就开始头脑中想象，是否每个点都把树分成了两半，只需要知道其中一半的大小即可
5.后来开始写算法，求解x节点的子树集合大小
6.从例子来看以为是完全二叉树，把二叉树和完全二叉树的定义搞混淆了，结果用了完全二叉树的性质求
解提交出现错误
7.然后发现应该拆开左右子树和父节点三块区域
8.思路基本明确。先找到x节点，然后递归方法求解左右子树大小
9.粗心导致变量名写错，出现了两次提交错误
10.最终AC
总结：题目猛一看有点吓到，稍微想了下很快有了思路。对二叉树和完全二叉树的定义有点混淆导致两次
wa。变量名写错导致两次wa

```

- 1240 Tiling a Rectangle with the Fewest Squares https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

```
这一道题猛一看感觉很有趣，也不难理解。第一反应是greedy，先用短边构建square，然后一次进行。
但是看了一下样例，似乎觉得这种方法不一定准确，尝试着在脑子中想象出反例以及构建反例的过程，发现
很难，失败放弃。
尝试着想从左下角开始构建square，然后余下的不规则图形想不出通用的处理方法

看了discussion后发现大家都有同样的苦恼，略感欣慰。当看有人提出来问题的出处，sqaureing 
sqaure后，才知道这道题本身就难度很高，不知道google onsite的时候出这道题是什么意图。

鉴于这道题难度较大，适用范围较窄，所以暂且搁置
```

- 1246 palindrome removal https://leetcode.com/problems/palindrome-removal/

```
2020/05/13
这是一道dp题，很容易看出来，但是如何剥离出来状态转移方程就比较困难，思考了好久都找不到答案。
我一直尝试用最后一次剥离的区间来做边界划分问题，但是发现始终没有办法整齐地把问题剥离开。

有时候又同时把两种剥离方法混淆在一起，一会想着用dp存储a,b区间的最有解，一会儿又想是否可以利用
最后一次range的边界信息来剥离问题。 可是一直没有捋清楚，最后这道题还是没有做出来。

后来我开始有了经验，如果一道题超过15分钟没有思路，很可能是缺乏一些知识点，如果寄希望于1个小时
的面试时间完全重新想出一个没有接触过的知识点，那基本是不可能的。 
所以当这个时候可以尝试着转换思路。

后来看了discussion，很巧妙，大家确实用了dp，但是剥离问题的方法不是用“最后一次消除的区间”，
而是就用dp存储把区间a到b整个消掉的最优解，（不是只以a，b为最后消除的边界）。这样的话问题就更
加容易利用转换的信息。可是这里面很巧妙的转移方法是通过分析边界a同时消除的idx作为划分的，跟先
后并无关系，这一个思想非常的巧妙，我恐怕再给我一个小时我也不一定想得出来。

后来一想，这是不是就是传说中的区间dp，可能我对区间dp没有一个整体的概念，所以没能很快地想出相
应的套路，或许这是做不出来的原因，赶紧把四大dp系统地复习一遍吧。
```

- 1255 Maximum Score Words Formed by Letters https://leetcode.com/problems/maximum-score-words-formed-by-letters/

```
2019/11/10
这道题其实很快有了思路，感觉是一个比较复杂的背包问题，因为资源有限，每个letter的个数是固定的
，而“物品”就是word，每个word花费的资源不同，也就是对26种letter的消费量不同，把word想成物品
，构建一个26维的背包，每个维度表示一个letter的资源量。 这种方法感觉应该没有问题。
可是implement起来遇到很大的麻烦，从来没有构建过26维的矩阵，尝试用26维的tuple来做key，但发
现也会比较麻烦。对于python自带的permutation的库不熟悉。

看了一下discussion，发现很多人利用了题目的一些限制，主要是数据量比较小这一点。。。
这个我从来没有想到过，作为竞赛项目，有时候要学会找到题目的一些限制条件从而找出一些小窍门。

又仔细做了以下这题，发现竟然看错题目了。score并不是表示letters 
list中的每个letter的值，而是分别表示26个字母的值
```

- 1261 Find Elements in a Contaminated Binary Tree https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

```
2019/11/17
这一题是weekly 163的第二道题，在我第一道题以前200名的速度成功提交后，还有点沾沾自喜。结果这
一道题阴沟里翻船。
首先第一反应这道题比较直白，没有多少弯子。
1.初始化无非就是一个递归，很简单
2.查值这个也是个很简单的问题，没有想太多，觉得也用递归的方法来做。脑子一瞬间闪过要把结果提前
存下来这个念头，可是担心太占内存，稍微估算了一下，大概100万个数，一瞬间脑残地认为这个值有点大
，怕是不存下来比较好，也没多想就写了个递归去查询。结果TLE

一下子给我惊呆了，心态差点崩掉。想着说这leetcode现在水涨船高啊，第二道题就给我TLE，有点牛逼
啊。于是我把问题又进一步想复杂了，然后再想一些其他的优化方法，比如如果避免即使剪枝停滞递归，结
果稍微尝试了两下感觉这个条件不是很好写，提交了还WA，心态都快不行了，想着说，先搁着吧，这第二
道题总不该这么难，先往下做。

第三题还算正常发挥做完后还剩不到20分钟，看了下第四题感觉这题属于真正比较复杂的，20分钟内AC恐
怕很难，所以就转头继续研究第二题。稍微想了下，想出来点剪枝方法，心里想，原来这个题目要考我这个
，还挺叼的。可是思路有了，最终还是没能成功AC，知道比赛结束后又琢磨了会才提了个AC的答案。

可是一看别人的讨论，直接呆逼了，别人都是直接把结果存在hashset里，find函数一句话搞定，差点一
口老血吐出来。
总结一下原因是自己对递归和hashset两者的复杂度没有一个较准确的直观了解。
我对树的递归基本每次都会遍历全树，而hashset的复杂的在O(1)，并且即使是所有结果全部存下来也不
过1M，所以内存占用并不大。

由于对各种数据结构的复杂度不够熟悉，并且习惯性把题目想复杂导致了这道题的失败。
```

- 1284 Minimum Number of Flips to Convert Binary Matrix to Zero Matrix https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

```
2019/12/08
这一道leetcode的周赛题，看完题目后，5分钟内就有了思路，觉得是到简单题，用二进制压缩，做一个d
fs即可。

然后不到10分钟就写出了第一个版本，
然后就开始进入持续将近一个小时的debug，debug，debug，，，

悲剧
本来还以为这次周赛必定AK，结果搞得这个下场。

debug的时候遇到几个点，直接没有那么清楚。
首先是bit压缩的时候，高位和低位如何存储数据这个问题，本来想着说靠前的item存储在高位，这样更
直观一些，结果发现操作的时候会有些不变。
然后就回到了把靠前的item存储在低位这个思路。折腾了半天。

还遇到一些问题，在debug的时候，由于不熟悉python的format对二进制的打印方法，中间来来回回也折
腾了半天。
最后才发现，问题竟然处在direction数组初始化的时候出错了。。。
前两天做了到8个方向遍历的题目，结果把斜线方向竟然也给写进去了。。。

唉，再接再厉，还是有差距。

把python的format再加强，还有bit压缩的题目再多练几道，把其中的小道道都摸透。
```

- 1367 Linked List in Binary Tree https://leetcode.com/problems/linked-list-in-binary-tree/

```
2020/03/01
这一题在周赛中，很快想到了用递归的方法，但是一提交前几个例子都没错，结果一个很长的测试样例出了
错误。
这一下子就僵住了，从代码上我怎么也没看出问题，而测试样例又给不出我有用的信息。

错误例子的输入太长，而且是树形结构，没法debug，一下就懵了。
盯着代码看了半天找不出来问题。。。
这一次的阴沟翻船，我总结了有两个问题。
1. 过于依赖测试样例进行debug，这在其他没有给测试样例的比赛中就没有用了。
如果这道题能够在简单输入上就给我报错，那么通过对这个样例进行debug，打印中间结果，我应该可以很
快的找出
问题所在，可是恰恰简单测试都通过了，唯一没通过的是一个巨大的输入。直接sb了。
2. 问题出在，递归的时候把整个链表的递归判断和部分链表的递归判断放在了一个递归函数。但是这里面
有一个问题，
链表head可以与数值不同，可以依次往树上继续遍历，可是一旦开始遍历head，就不能再有数值不相等的
情况，否则
应该返回false，我没有把这两个区分开，写在了一个递归中，结果出错。

以后要减少依赖测试样例做debug，尽量在写的时候保证思路清晰，直接写出正确答案，不要过于依赖测试
结果给的信息。
关于链表还是会犯一些简单的错误，对链表和树的处理没有达到那么熟练。

根本问题还是错误的例子过长，无法debug。。。

3. 以后要习惯自己设计测试样例，自己对自己进行测试，不要过于依赖别人提供的测试，这也是写代码中
必备的一个技能。
```

- 1438 longest continuous subarray with absolute diff less than or equal to limit https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
2020/05/10

- 1439 find the kth smallest sum of matrix with sorted rows https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

```
2020/05/03
I failed this problem in 2020/05/03 weekly contest, I skipped the 3rd problem 
and started to solve this one directly, I was confident enough 
to solve it, but after spent around 1 hour, still could not figure out the 
trick and estimate how many combinations there are in total.

I was very close to the right direction, but my head was too dizzy and lazy to 
clear it out, I thought I maybe was sleepy at that moment? 
I forgot what I did the day before that day, maybe slept very late. 

I got the first idea of using heap in 5 minutes, but I wrongly thought I just 
needed to add the next value of the row of the popped item.
I mistook for the concept of selecting one item from each row and calculate 
the sum. 
```

- 1453 maximum number of darts inside of a circular dartboard https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/


2020/05/17

	这一道题猛一看，似乎像是之前做过的，但再细看发现不是。 我尝试着遍历平面上所有的点，然后以该点为圆心，计算此圆包含的点数，结果超时了。然后感觉找不到思路，从来没有正式做过这一类的几何题，有点没有头绪，网上查了一下看看有一种n^3的方法，然后看了下题目的数据大小，发现应该没问题。

	思路很简单，任意找两个点，计算以r为半径，过这两点的圆弧，得到一个圆心。然后统计个数。
	感觉思路很简单，但是计算圆心牵涉到浮点数计算有些麻烦，最后实现完有个case过不了。

结果看了别人的答案，才知道原来需要处理浮点计算导致的误差，需要加上一个很小的epsilon 1e-8 来
判断==的情况。

以后要适当练习一下计算几何类的题目。


- 1262 Greatest Sum Divisible by Three https://leetcode.com/problems/greatest-sum-divisible-by-three/

```
2019/11/17
这一题一开始用dp，但是写了个两层循环，每次都和之前所有元素的情况做了一次对比，结果导致超时，
当时也是一下子心态差点崩。而事实上如果稍微仔细想一下的话就知道因为在意的只有除3余数的三种情况
，0，1，2，根具体之前的某个数值关系并不大，只需要每次更新这个0，1，2的数组，用最当下最大值替
代即可，从头遍历实在是多此一举，直接导致TLE。

反思一下，做题不能过于盲目的使用套路，竟可能先想想最优解。 而这一题主要是没想到连dp都会TLE
```