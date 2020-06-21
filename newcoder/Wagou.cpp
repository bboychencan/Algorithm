#include <iostream>
#include <algorithm>
using namespace std;
    
int const N = 1e5 + 5;
int const M = 5e5 + 5;
int parent[N]; 

struct node{
    int a, b, c;
    bool operator < (const node r){
        return c < r.c;
    }
} edges[M];

int find(int x){
    // cout << parent[x] << endl;
    if(parent[x] == -1){
        return x;
    }
    parent[x] = find(parent[x]);
    return parent[x];
}

int main(){
    int n, m;
    cin >> n >> m;
    for(int i=0; i<n; i ++) parent[i] = -1;
    for(int i=0; i<m ;i++){
        int a, b, c;
        // scanf("%d%d%d", &a, &b, &c);
        // edges[i] = {a, b, c};
        cin >> edges[i].a >> edges[i].b >> edges[i].c;
    }
    sort(edges, edges + m); 
    int res = 0;
    int count = 0;

    for(int i=0; i<m ;i++){
        int x = find(edges[i].a);
        int y = find(edges[i].b);
        if(x == y) continue;
        parent[x] = y;
        count += 1;
        res += edges[i].c;
        if(count == n - 1){
            cout << res << endl;
            return 0;
        }
    }
    return 0;
};