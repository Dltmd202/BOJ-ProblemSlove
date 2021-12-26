#include <vector>
#include <queue>
#include <iostream>


using namespace std;


int main(){
    int f, s, g, u, d;
    cin >> f >> s >> g >> u >> d;

    bool *visit = (bool *)malloc(sizeof(bool) * (f + 1));
    visit[s] = 1;

    queue<pair<int, int>> q;
    q.push(make_pair(s, 0));
    int answer = -1;
    int now = 0;
    int cnt = 0;
    while (!q.empty()){
        now = q.front().first;
        cnt = q.front().second;
        q.pop();
        if (now == g){
            answer = cnt;
            break;
        }
        if (now + u <= f){
            if (!visit[now + u]){
                q.push(make_pair(now + u, cnt + 1));
                visit[now + u] = true;
            }
        }
        if (0 < now - d){
            if (!visit[now - d]){
                q.push(make_pair(now - d, cnt + 1));
                visit[now - d] = true;
            }
        }
    }
    if (answer == -1){
        cout << "use the stairs";
    }
    else{
        cout << answer;
    }
}