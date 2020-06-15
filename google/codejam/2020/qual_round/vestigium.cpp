#include <iostream>
#include <vector>
#include <set>
using namespace std;

int grid[1005][1005];

void test_case(){
	int n;
	scanf("%d", &n);
	// set<int> x;
	long long trace = 0;
	vector<set<int> > row(n + 1), col(n + 1);
	for(int i=1; i<=n; i++){
		for(int j=1 ; j<=n; j++){
			scanf("%d", &grid[i][j]);
			row[i].insert(grid[i][j]);
			col[j].insert(grid[i][j]);
			if(i == j){
				trace += grid[i][j];
			}
		}
	}
	int bad_rows = 0, bad_cols = 0;
	for(int i = 1; i <= n; i++){
		if(row[i].size() != n){
			bad_rows += 1;
		}
		if(col[i].size() != n){
			bad_cols += 1;
		}

	}
	printf("%lld %d %d\n", trace, bad_rows, bad_cols);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; i++){
		printf("Case #%d: ", i);
		test_case();
	}
}