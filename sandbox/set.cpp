#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int getNext(int n){
        int ans = 0;
        while(n > 0){
            int d = n % 10;
            n /= 10;
            ans += d * d;
        }    
        return ans;
    }
    
    bool isHappy(int n) {
        set<int> set;
        while(set.find(n) == set.end()){
            printf("%d",n);
            set.insert(n);
            n = getNext(n);
            if(n == 1){
                return true;
            }
        }
        return false;
    }
};

int main(){
    int arr[] = {3,2,1,4,3,2,1};
    set<int> s (arr, arr + 7);

    for(auto x: s){
        
    }
}