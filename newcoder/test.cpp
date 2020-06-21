#include <cstdio>
#include <iostream>
#include <algorithm>
 
using namespace std;
typedef long long int LL;
 
const int N = 100010, M = 500010;
int p[N];
int n,m;
struct Edge{
    int a, b, v;
    bool operator< (const Edge & ver)
    {
        return v < ver.v;
    }
}Edges[M];
 
int find(int x)
{
    if(x != p[x]) p[x] = find(p[x]);
    return p[x];
}
 
int main(void)
{
    scanf("%d%d", &n, &m);
    for(int i=1;i<=n;i++) p[i] = i;
    for(int i=0;i<m;i++)
    {
        int a,b,v;
        scanf("%d%d%d", &a, &b, &v);
        Edges[i] = {a,b,v};
    }
    sort(Edges, Edges + m);
     
    LL res = 0;
    for(int i=0;i<m;i++)
    {
        int a=Edges[i].a ,b = Edges[i].b, v = Edges[i].v;
        a = find(a), b = find(b);
        if(a != b)
        {
            p[a] = b;
            res += v;
        }
    }
    cout << res << endl;
}