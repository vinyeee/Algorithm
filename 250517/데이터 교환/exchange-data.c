#include <stdio.h>

int main() {
    // Please write your code here.
    int a = 5, b = 6, c = 7;
    int temp = b;
    b = a;
    a = c;
    c = temp;

    printf("%d\n%d\n%d", a, b, c);
    return 0;
}