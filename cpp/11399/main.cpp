//11399
//https://www.acmicpc.net/problem/11399

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> data;
    vector<int> prefix;
    int answer = 0;
    int part = 0 ;
    for (int i = 0 ; i < n ; i++){
        int buff; cin >> buff;
        data.push_back(buff);
    }
    sort(data.begin(),data.end());

    for (int i = 0; i < n ; i++) {
        part += data[i];
        answer += part;
        prefix.push_back(part);
    }
    cout << answer;



}
