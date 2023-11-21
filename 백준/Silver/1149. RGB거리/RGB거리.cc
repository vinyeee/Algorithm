#include <bits/stdc++.h>
using namespace std;

int dp[1001][3]; // 테이블1 : 
int r[1001] , g[1001] , b[1001]; // 테이블 2

int main(){

    int n; // n개의 집
    cin >> n;

    for(int i=1; i<=n; i++){
        cin >> r[i] >> g[i] >> b[i];// i번째 집을 각 색깔로 칠하는데 드는 비용    
    }

    dp[1][0] = r[1]; // 첫 번째 집을 r로 칠하는데 필요한 비용
    dp[1][1] = g[1]; // 첫 번째 집을 g로 칠하는데 필요한 비용
    dp[1][2] = b[1]; // 첫 번째 집을 b로 칠하는데 필요한 비용

    for(int i = 2; i <= n; i++){
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r[i]; // i번째 집을 빨간색으로 칠하기 위한 최솟값
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g[i];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b[i];
    }

    cout << min({dp[n][0], dp[n][1] , dp[n][2]});


}