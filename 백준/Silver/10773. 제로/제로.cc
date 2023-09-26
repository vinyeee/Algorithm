#include <bits/stdc++.h>

using namespace std;

int stackSum(stack<int> stack){
    int sum = 0;

    if(stack.empty()){
       return 0; 
    }else{
        int size =  stack.size(); 
        for (int i = 0; i < size; i++)
        {
            //cout << "top: " << stack.top() << '\n';
            sum += stack.top();
            stack.pop();
        }

        return sum;
    }
}

int main(){

    ios:: sync_with_stdio(false);
    cin.tie(0);

    stack<int> stack;

    int k; cin >> k; // 재현이가 부르는 수의 개수 
    int n; 

    for (int i = 0; i < k; i++){
        cin >> n;
        if (!n == 0){
            stack.push(n);
        }else{
            stack.pop();
        }
    }

    cout << stackSum(stack);


}