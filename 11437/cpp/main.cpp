#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<int> graph[50001];
int parent[50005];
int d[50005];
int v[5005];

void dfs(int x, int depth){
    v[x] = 1;
    d[x] = depth;
    for (int y : graph[x]){
        if (!v[y]) {
            parent[y] = x;
            dfs(y, depth + 1);
        }
    }
}

int lca(int a, int b){
    while (d[a] != d[b]){
        if (d[a] > d[b]) a = parent[a];
        else b = parent[b];
    }
    while (a != b){
        a = parent[a];
        b = parent[b];
    }
    return a;
}


int main() {
    int n, m;
    cin >> n;

    for (int i = 0; i < n - 1; i ++ ){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(1, 0);
    cin >> m;
    int answer[m + 1];
    for (int i = 0; i < m; i ++){
        int a,b;
        cin >> a >> b;
        answer[i] = lca(a, b);
    }
    for (int i = 0; i < m; i++){
        printf("%d\n",answer[i]);
    }
}
