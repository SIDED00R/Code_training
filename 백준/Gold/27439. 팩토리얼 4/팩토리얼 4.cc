#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll a[500000] = { 1 };
int sz = 1;
const ll mod = 10000000000000;

int main()
{
	int n;
	cin >> n;
	int i, j;
	for (i = 2; i <= n; i++)
	{
		ll x = 0;
		for (j = 0; j < sz; j++)
		{
			a[j] = a[j] * i + x;
			x = a[j] / mod;
			a[j] %= mod;
		}
		if (x)
			a[sz++] = x;
	}
	printf("%lld", a[--sz]);
	for (sz--; sz >= 0; sz--)
		printf("%013lld", a[sz]);
}