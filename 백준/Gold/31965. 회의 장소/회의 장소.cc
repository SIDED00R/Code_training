#include <stdio.h>
#include <algorithm>

using namespace std;

int n, q, l, r;
long long X[200010], P[200010];
long long getCost(int i, int j, int k) {
    long long leftCost = (long long)(k - i + 1) * X[k] - (P[k] - P[i - 1]);
    long long rightCost = (P[j] - P[k - 1]) - (long long)(j - k + 1) * X[k];
    
    return leftCost + rightCost;
}

int main() {

    scanf("%d%d", &n, &q);
    

    for (int i = 1 ; i <= n ; ++i) {
        scanf("%lld", &X[i]);
        P[i] = P[i - 1] + X[i];
    }
    

    while (q--) {
        scanf("%d%d", &l, &r);

        int lo = lower_bound(X + 1, X + n + 1, l) - X;
        int hi = upper_bound(X + 1, X + n + 1, r) - X - 1;
        
        if (lo >= hi) {
            puts("0");
        } else {
            long long maxStress = max(getCost(lo, hi, lo), getCost(lo, hi, hi));
            long long minStress = getCost(lo, hi, (lo + hi) / 2);
            
            printf("%lld\n", maxStress - minStress);
        }
    }
}