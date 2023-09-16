#include <iostream>
#include <stack>
#include <string>

using namespace std;

// 연산자의 우선순위를 반환하는 함수
int getPriority(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int main() {
    string infix;
    cin >> infix;

    stack<char> operatorStack;
    string postfix = "";

    for (char token : infix) {
        if (isalpha(token)) {
            // 피연산자인 경우 바로 출력
            postfix += token;
        } else if (token == '(') {
            // 여는 괄호인 경우 스택에 푸시
            operatorStack.push(token);
        } else if (token == ')') {
            // 닫는 괄호인 경우 여는 괄호를 만날 때까지 스택에서 연산자를 팝하고 출력
            while (!operatorStack.empty() && operatorStack.top() != '(') {
                postfix += operatorStack.top();
                operatorStack.pop();
            }
            operatorStack.pop(); // 여는 괄호 제거
        } else {
            // 연산자인 경우 우선순위를 고려하여 스택에 푸시
            while (!operatorStack.empty() && getPriority(operatorStack.top()) >= getPriority(token)) {
                postfix += operatorStack.top();
                operatorStack.pop();
            }
            operatorStack.push(token);
        }
    }

    // 스택에 남아있는 모든 연산자를 출력
    while (!operatorStack.empty()) {
        postfix += operatorStack.top();
        operatorStack.pop();
    }

    cout << postfix << endl;

    return 0;
}