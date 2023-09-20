#include <iostream> 

using namespace std;

int main(){
    while(true){
        int n1; cin >> n1;
        int n2; cin >> n2;
        if(n1 == 0 && n2 == 0){
            break;
        }else if (n1 <= n2)
        {
            cout << "No" << endl;
        }else if(n1 > n2){
            cout << "Yes" << endl;
        }
    }
}