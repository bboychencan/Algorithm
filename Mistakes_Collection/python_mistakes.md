# Python Mistakes

python使用时的注意事项 *leetcode刷题经验


#1 对数组 index的时候

x[5:3] 这种不会输出逆序排列的子数组，只会输出空数组[]

#2 比如如果
A = [[0] * 100] * 100
那么A[0][0] = 1 赋值的时候，会导致第一列全部为1

更好的方法是
A = [[0 for i in range(100)] for i in range(100)]


#3 max函数可以直接比较字符串
如max(‘abc’, ‘aced’)

#4关于强连通图的概念，Tarjan算法

#5 python for/else 用法样例

 found_obj = None
for obj in objects:
    if obj.key == search_key:
        found_obj = obj
        break
else:
    print('No object found.’)


#6 python global virable
        stack = []
        low = [0] * n
        DFN = [0] * n
        visited = [0] * n
        count = 1

        res = []
        stack.append(0)
        low[0] = 1
        DFN[0] = 1


        def tarjan(start: int):
            for node in paths[start]:
                if node not in stack and visited[node] == 0:
                    count = count + 1
                    DFN[node] = count

UnboundLocalError: local variable 'count' referenced before assignment

这个情况比较奇怪，同样是在inner函数外部定义的变量，stack，DFN，visited等数组变量可以直接在inner函数内部使用，但是count就会被认为是没有定义
这是因为
Python scoping rules 101:
1. a name bound in a function body is considered local unless explicitely declared global (Python 2.x and 3.x) or nonlocal (Python 3.x only). This holds true whereever the assignment happens in the function's body. Trying to read a local variable before it's bound is of course an error.
2. if a name is read but not bound in a function's body, it will be looked up in enclosing scopes (outer function(s) if any then global scope). NB: functions arguments are de facto local names so they will never be looked up in enclosing scopes.
一种可能的hack方法就是把这个变量用一个mutable变量包裹wrap the variable in a mutable，比如count  = [0]，这样就可以改变他。 所以也是为什么count不可以改，而其他数组变量可以改变
