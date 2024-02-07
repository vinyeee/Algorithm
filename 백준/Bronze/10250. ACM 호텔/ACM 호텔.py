i = int(input())


for _ in range(i):
    h,w,n = map(int,input().split()) #높이, 너비, n번째 방문자
    
    y = h if n % h == 0 else n % h  #층수 
    x = (n // h) if (n % h) == 0 else (n // h) + 1  #맨 꼭대기일 땐 몫 그대로 호수, 나머지는 +1  
    print('{}{:02d}'.format(y,x)) 
