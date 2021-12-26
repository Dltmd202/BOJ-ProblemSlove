#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <math.h>

#define MOD 1000000007

using namespace std;
typedef long long ll;
vector<ll> inits;

void init(vector<ll> &tree, int node, int start, int end, int idx, int val){
    if (start > idx || end < idx)
        return;
    if (start == end){
        tree[node] = val % MOD;
        return;
    }
    int mid = (start + end) / 2;
    init(tree, node * 2, start, mid, idx, val);
    init(tree, node * 2 + 1, mid + 1, end, idx, val);
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD;
}

ll query(vector<ll> &tree, int node, int start, int end, int left, int right){
    if (left > end || start  > right){
        return 1;
    }
    if (left <= start && end <= right){
        return tree[node];
    }
    int mid = (start + end) / 2;
    return (query(tree, node * 2, start, mid, left, right) * query(tree, node * 2 + 1, mid + 1, end, left, right)) % MOD;
}

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    int h = (int)ceil(log2(n)) + 1;
    int size = (1 << h);
    int start = 0;
    int end = (1 << (h - 1)) - 1;
    vector<ll> tree(size);
    for(int i = 0; i < n; i ++){
        int val;
        scanf("%d", &val);
        init(tree, 1, start, end, i, val);
    }
    for(int i = 0; i < m + k; i ++){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        if (a == 1){
            init(tree, 1, start, end, b - 1, c);
        }
        else if (a == 2){
            printf("%lld\n", query(tree, 1, start, end, b - 1, c - 1));
        }
    }
}
