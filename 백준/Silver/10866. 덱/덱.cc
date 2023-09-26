

#include <bits/stdc++.h>

using namespace std;

int main(){

    int n; cin >> n; // 명령의 수
    string cmd;
    int val;

    ios::sync_with_stdio(false);
    cin.tie(0);
    
    deque<int> dq; // deque 선언 삽입과 삭제가 양쪽에서 다 일어날 수 있음

    for (int i = 0; i < n; i++){

        cin >> cmd;
        if (cmd == "push_front"){
            cin >> val; 
            dq.push_front(val);
            
        }else if(cmd == "push_back"){
            cin >> val;
            dq.push_back(val);
        }else if(cmd == "pop_front"){
            if (!dq.empty()){
                // dq에 값이 존재하면 
                cout << dq.front() << '\n';
                dq.pop_front();
            }else{
                cout << -1 << '\n'; 
            }
        }else if(cmd == "pop_back"){
            if(!dq.empty()){
                cout << dq.back() << '\n';
                dq.pop_back();
            }else{
                cout << -1 << '\n';
            }
        }else if(cmd == "size"){
            cout << dq.size() << '\n';
        }else if(cmd == "empty"){
            if(dq.empty()){
                cout << 1 << '\n';
            }else{
                cout << 0 << '\n';
            }
        }else if(cmd == "front"){
            if(!dq.empty()){
                cout << dq.front() << '\n';
            }else{
                cout << -1 << '\n';
            }
        }else if(cmd == "back"){
            if(!dq.empty()){
                cout << dq.back() << '\n';
            }else{
                cout << -1 << '\n';
            }
        }

        
    }



}
