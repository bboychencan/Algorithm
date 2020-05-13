# 381. Insert Delete GetRandom O(1) - Duplicates allowed


这一题考察对底层数据结构的了解。

2年前尝试过这道题，没解出来，现在2020/05/13重新看这道题的时候，很快想到用python里面的counter去存储每个元素的频率。至于说随机抽样，查了一下，python里面有random.choices with weights，即可以根据weights来进行抽样。 可是这里面有一个问题，random.choices只能对支持indexing的结构操作。 而set本身不支持这个。
我第一反应就是直接把set转成list不就行了嘛，一行代码的事。 可是忘了考虑这个操作是需要O(n)
的。 虽然代码写起来很快，但是其实效率不高，面试的时候很可能会被挂在这。

后来看了下别人的解，才发现一个非常巧妙的方法，那就是用一个dict来存储每个元素所在的所有index，另外一个数组来存储所有元素。
数组可以用来抽样，插入操作只需要把元素append到数组末尾，而remove操作就很巧妙了，通过记录的val在dict中的index值，交换数组index处和数组末尾处的值，然后把nums数组删除最后一位即可。

这个方法非常地聪明，值得学习。