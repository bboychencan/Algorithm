T = int(input())

for x in range(1, T + 1):
    a, b = list(map(int, input().split()))
    # print(a,b)
    n = int(input())
    a = 1
    mid = (a + b) // 2

    for i in range(n):
        print(mid)
        s = input()
        if s == "TOO_BIG":
            b = mid - 1
            mid = (a + b) // 2
        elif s == "TOO_SMALL":
            a = mid + 1
            mid = (a + b) // 2
        elif s == "CORRECT":
            break
