#include <bits/stdc++.h>

using namespace std;
vector<int> table;
void create_table(string pattern){
    table.clear();
    table.resize(pattern.size());
    int length = pattern.size();
    int j = 0;
    for (int i = 1; i < length; i++){
        while (j >0 && pattern[i] != pattern[j]){
            j = table[j - 1];
        }
        if (pattern[i] == pattern[j]){
            table[i] = ++j;
        }
    }
}

bool kmp(string parent, string pattern){
    create_table(pattern);
    int parent_size = parent.size();
    int pattern_size = pattern.size();
    int j = 0;
    bool result = false;
    for (int i = 0; i < parent_size; i ++){
        while (j > 0 && parent[i] != pattern[j]){
            j = table[j - 1];
        }
        if (parent[i] == pattern[j]){
            if (j == pattern_size - 1){
                if (result){
                    return false;
                }
                result = true;
                j = table[j];
            }
            else{
                j ++;
            }
        }
    }
    return result;
}

string a, w, s;
int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc ++){
        cin >> a >> w >> s;
        map<char, char> conv;
        vector<int> answer;
        for (int i = 0; i < a.size(); i ++){
            conv[a[i]] = a[(i + 1) % a.size()];
        }
        for (int shift = 0; shift < a.size(); shift ++){
            if (shift != 0){
                for (int j = 0; j < a.size(); j ++){
                    w[j] = conv[w[j]];
                }
            }
            bool result = kmp(s, w);
            if (result){
                answer.push_back(shift);
            }
        }
        if (answer.empty()) {
            cout << "no solution" << '\n';
        }
        else if (answer.size() == 1) {
            cout << "unique: " << answer[0] << '\n';
        }
        else {
            cout << "ambiguous: ";
            for (int x : answer)
                cout << x << ' ';
            cout << '\n';
        }
    }
}
