
H , M = map(int,input().strip().split())

if (M < 45):

    H = H - 1 # 60진법 사용해서 H에서 1하나 빼주기
    if (H < 0): #이 때 만약 H가 음수라면 
        H = 23 # 이전날 23시로 setting
    M += 60 - 45 # 60 더하고 다시 - 45분 

else:
    M -= 45
print(f"{H} {M}")