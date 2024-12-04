a,b,c,d = map(int, input().split())


def elapsed_time(h, m):
    hour = 0
    mins = 0
    t= 0
    while True:
        if hour == h and mins == m:
            break
        
        t += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0 
    return t

print(elapsed_time(c , d) - elapsed_time(a , b))