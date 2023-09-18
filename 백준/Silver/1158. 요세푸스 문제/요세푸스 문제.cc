#include <iostream>
#include <queue>

using namespace std;

int main(){
    int n,k; 
    cin >> n >> k;

    queue<int> q; // 비어있는 큐 선언
    for(int i = 1; i <= n; i++){
        q.push(i);
    }

    cout << "<";
    while(!q.empty()){ // 큐가 비어있을 때까지 반복
        for(int i = 0; i < k - 1; i++){
            q.push(q.front());
            q.pop();
        }

        cout << q.front();
        q.pop();
        if(!q.empty()){
            cout << ", ";
;        }

    }

    cout << ">";

    return 0;
}

