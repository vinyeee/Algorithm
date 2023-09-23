#include <bits/stdc++.h>


using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(0);

    long long S; cin >> S;

    for(long long i = 0; i <= S; i++){
        if((i * ( i + 1 )) / 2 > S){
            cout << i - 1 << endl;
            break;
        }else if( i * ( i + 1 ) / 2 == S){
            cout << i << endl;
            break;
        }
    }


}