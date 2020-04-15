#include <vector>
#include <iostream>
using namespace std;


void pass_reference(vector<int>& s){
	vector<int> temp = {3,4,5};
	// s[0] = 1000;
	s[0] = 100;
	// s = temp;
	// s = &temp;
	// s = new vector<int>();
}

void pass_ref_int(int& a){
	a = 100;
}

void pass_value(vector<int> s){
	vector<int> temp = {3,2,1};
	s[0] = 100;
}

int main(){
	vector<int> v = {1,2,3};
	cout << "before passing" << endl;
	for(auto x: v){
		cout << x << endl;
	}
	cout << "after passing" << endl;
	pass_reference(v);
	// pass_value(v);
	for(auto x : v){
		cout << x<< endl;
	}
}