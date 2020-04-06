T = int(input())

def peel(s, dep):
    if s == "": return s
    mini = int(min(s))
    dep += mini
    temp = "".join([str(int(s[i]) - mini) for i in range(len(s))])
    arr = temp.split('0')
    for i in range(len(arr)):
        arr[i] = peel(arr[i], dep)
    res = "(" * mini + str(dep).join(arr) + ")" * mini
    return res

for  x in range(T):
    s = input()
    res = peel(s, 0)
    print("Case #{}: {}".format(x, res))
    