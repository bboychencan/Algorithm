T = int(input())

for x in range(1, T+1):
    n = int(input())
    acts = []
    for i in range(n):
        s, e = list(map(int, input().split()))
        acts.append([s,e,i])
    seqs = sorted(acts, key=lambda x: (x[0], x[1]))
    cact = None
    jact = None

    res = ["*" for i in range(n)]
    for i in range(n):

        if not cact:
            cact = (seqs[i][0], seqs[i][1])
            res[seqs[i][2]] = 'C'
        elif not jact:
            jact = (seqs[i][0], seqs[i][1])
            res[seqs[i][2]] = 'J'
        else:
            sc, ec = cact
            if seqs[i][0] >= ec:
                cact = (seqs[i][0], seqs[i][1])
                res[seqs[i][2]] = 'C'
            else:
                sj, ej = jact
                if seqs[i][0] >= ej:
                    jact = (seqs[i][0], seqs[i][1])
                    res[seqs[i][2]] = 'J'
                else:
                    res = "IMPOSSIBLE"
                    print("Case #{}: {}".format(x, res))
                    break

    else:
        res = "".join(res)
        print("Case #{}: {}".format(x, res))


    
