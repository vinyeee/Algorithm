'''
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.


'''
import sys
a = int(input())
b = input()

n1 =  int(b[2])
n2 =  int(b[1])
n3 =  int(b[0])
b =  int(b)

print(a * n1)
print(a * n2)
print(a * n3)
print(a * b)

