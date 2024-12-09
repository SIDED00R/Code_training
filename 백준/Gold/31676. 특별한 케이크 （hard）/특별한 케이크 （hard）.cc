#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;
int cnt[123456], lb;
vector<int> tmp;
int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
	string dm; getline(cin, dm);
	int n; cin >> n;
	for(int i = 1; i <= n; i++){
		int m; cin >> m;
		tmp.clear();
		while(m--){
			int s; cin >> s;
			tmp.push_back(s);
		}
		int b; cin >> b;
		if(b){
			for(auto s : tmp){
				cnt[s]++;
				if(s == i) cnt[s] = -1234567;
			}
		}
		else{
			lb--;
			bool f = 1;
			for(auto s : tmp){
				cnt[s]--;
				if(s == i) f = 0;
			}
			if(f) cnt[i] = -1234567;
		}
	}
	vector<int> ans;
	for(int i = 1; i <= n; i++) if(cnt[i]-lb == n-1) ans.push_back(i);
	if(ans.empty()) cout << "swi";
	else for(auto i : ans) cout << i << ' ';
}