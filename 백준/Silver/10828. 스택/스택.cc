#include <bits/stdc++.h>


using namespace std;

int main(){
    
    
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;

    stack<int> stack;
    
    for(int i = 0; i < N; i++){

        string cmd; cin >> cmd;
        
        if(cmd == "push"){
            int val; cin >> val;
            stack.push(val);
        }
        else if(cmd == "pop"){
            if(stack.empty()){
                cout << -1 << '\n';
            }else{
                cout << stack.top() << '\n';
                stack.pop();
            }
        }else if(cmd == "top"){
            if (stack.empty()){
                cout << -1 << '\n';
            }else{
                cout << stack.top() << '\n';
            }
        }else if(cmd == "size"){
            cout << stack.size() << '\n';
            
        }else if( cmd == "empty"){
            if (stack.empty()){
                cout << 1 << '\n';
            }else{
                cout << 0 << '\n';
            }
        }

    }



}

