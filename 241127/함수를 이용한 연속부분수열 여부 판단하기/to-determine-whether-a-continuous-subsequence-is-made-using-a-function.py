n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_part_series(a,b):
    try: 
        idx = a.index(b[0])
    except Exception :
        return "No"
    
    b_idx = 0
    for i in range(idx,idx + len(b)):
        if a[i] != b[b_idx]:
            return "No"
        b_idx += 1
    return "Yes"


if n1 > n2:
    print(is_part_series(a, b))
else:
    print(is_part_series(b, a))

