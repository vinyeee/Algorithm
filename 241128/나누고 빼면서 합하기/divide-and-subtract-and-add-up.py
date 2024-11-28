n,m = map(int, input().split())
a = list(map(int, input().split()))



def add_arr_m_index(m): 
    sum = 0
    while m >= 1 :
        sum += a[m - 1]        
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
    return sum 


print(add_arr_m_index(m))
        



