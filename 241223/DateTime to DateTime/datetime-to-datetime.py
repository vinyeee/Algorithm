d2, h2 ,m2 = map(int, input().split())




def elapsed_time(d2, h2 ,m2):

    d1, h1 ,m1 = 11, 11, 11

    t = 0
    while True:

        if d1 > d2 or (d1 == d2 and h1 > h2 ) or (d1 == d2 and h1 == h2 and m1 > m2):
            return -1 
            
        if d1 == d2 and h1 == h2 and m1 == m2:
            return(t)

        t += 1
        m1 += 1

        if m1 >= 60:
            h1 += 1 
            m1 = 0 
            if h1 >= 24:
                d1 += 1
                h1 = 0 

print(elapsed_time(d2, h2, m2))

    



