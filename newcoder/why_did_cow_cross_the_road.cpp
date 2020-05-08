#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int n;
	cin >> n;
	int l[n], r[n];
	int dp[n+1];
	int pre[n+1];
	memset(dp,0, sizeof(dp));
	memset(pre, 0, sizeof(pre));
	for(int i=0; i<n; i++){
		cin >> l[i];
	}
	for(int i=0; i<n; i++){
		cin >> r[i];
	}
	for(int i=n-1; i>=0; i--){
		for(int j=n-1; j>=0; j--){
			int temp = 0;
			if(abs(l[i] - r[j]) <= 4){
				temp = max(temp, pre[j+1] + 1);
			}else{
				temp = max(temp, pre[j+1]);
			}
			temp = max(temp, pre[j]);
			temp = max(temp, dp[j+1]);
			dp[j] = temp;
		}
		
		copy(dp, dp+n+1, pre);
		memset(dp, 0, sizeof(dp));
		
	}
	cout << pre[0] << endl;
	return 0;
}