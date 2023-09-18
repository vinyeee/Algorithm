#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main(){

    queue<int> q;

    int n; cin >> n;
    for(int i = 0; i < n; i++){
        string cmd; cin >> cmd;
        if (cmd == "push"){
            int val; cin >> val;
            q.push(val);

        }else if(cmd == "pop"){
            if (!q.empty()){ // 큐가 비어있지 않을 때
                cout << q.front() << endl;
                q.pop();
            }else{ // 큐가 비어있으면 -1 출력
                cout << -1 << endl;
            }
        }else if(cmd == "size"){
            cout << q.size() << endl;
        }else if(cmd == "empty"){
            if(!q.empty()){
                cout << 0 << endl;
            }else{
                cout << 1 << endl;
            }
        }else if(cmd == "front"){
            if(!q.empty()){
                cout << q.front() << endl;
            }else{
                cout << -1 << endl;
            }
        }else if(cmd == "back"){
            if(!q.empty()){
                cout << q.back() << endl;
            }else{
                cout << -1 << endl;
            }
        }
    }


    return 0;
}