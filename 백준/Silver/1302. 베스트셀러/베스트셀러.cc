#include <bits/stdc++.h>

using namespace std;

string selectBestseller(map<string, int> bookCount) {
    int maxBookCount = 0;
    string bestseller;

    for (const auto& book : bookCount) {
        if (book.second > maxBookCount) {
            maxBookCount = book.second;
            bestseller = book.first;
        } else if (book.second == maxBookCount && book.first < bestseller) {
            // 판매 횟수가 동일한 경우 사전 순으로 더 작은 책 제목을 선택
            bestseller = book.first;
        }
    }

    return bestseller;
}

int main() {
    int N;
    cin >> N;
    map<string, int> bookCount; // 각 책이 몇 권 팔렸는지 저장

    string book;

    for (int i = 0; i < N; i++) {
        cin >> book;
        bookCount[book]++;
    }

    // 가장 많이 팔린 책 찾기
    cout << selectBestseller(bookCount);

    return 0;
}