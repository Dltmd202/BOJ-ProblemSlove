#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <math.h>

#define INF 1e10

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
int cnt = 0;

void init(vector<ll> &tree, vector<ll> &items, int node, int start, int end){
    if (start == end){
        tree[node] = items[start];
        return;
    }
    int mid = (start + end) / 2;
    init(tree, items, node * 2, start, mid);
    init(tree, items, node * 2 + 1, mid + 1, end);
    tree[node] = tree[node * 2];
}

ll query(vector<ll> &tree, int node, int start, int end, int left, int right){
    if (start > right || left > end){
        return 0;
    }
    if (left <= start and end <= right){
        return tree[node];
    }
    int mid = (start + end) / 2;
    return query(tree, node * 2, start, mid, left, right) + query(tree, node * 2 + 1, mid + 1, end, left, right);
}

int main() {
    int n;
    cin >> n;
    int h = (int)ceil(log2(n)) + 1;
    int size = (1 << h);
    int end = (1 << (h - 1)) - 1;
    int start = 0;
    int node = 1;
    vector<ll> tree(size, INF);
    vector<ll> items(n + 1, INF);
    for(int i = 0; i < n; i ++){
        ll item;
        scanf("%lld", &item);
        items[i] = item;
        cout << items[i] << endl;
    }
    cout << items[3] << endl;
    init(tree, items, node, start, end);
    for(int i = 0; i < size; i ++){
        cout << tree[i] << endl ;
    }
}
