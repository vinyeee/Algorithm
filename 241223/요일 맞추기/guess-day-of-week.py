m1 , d1, m2, d2 = map(int, input().split())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]

def num_of_days(m, d):
    
    today = 0
    for i in range(1, m):
        today += month[i]

    today += d

    return today


diff = num_of_days(m2,d2) - num_of_days(m1, d1)

print(days[diff % 7])