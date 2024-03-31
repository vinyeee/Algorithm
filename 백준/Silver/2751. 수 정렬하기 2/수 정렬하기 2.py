import sys

n = int(sys.stdin.readline().strip())
A = [int(sys.stdin.readline()) for _ in range(n)]
#print(A)

def merge(L,R):
    i,j = 0,0 
    sorted_list = []

    for k in range(len(L) + len(R)):
        if i < len(L) and j < len(R): 
            if L[i] <= R[j]:
                sorted_list.append(L[i])
                i += 1
            else:
                sorted_list.append(R[j])
                j += 1 
        else :
            if i >= len(L):
                sorted_list.append(R[j])
                j += 1
            elif j >= len(L):
                sorted_list.append(L[i])
                i += 1

    return sorted_list

def merge_sort(A): #배열 A, start, mid, end
    #크기가 1 이하면 반환
    if len(A) < 2:
        return A
    # 리스트를 2분할 => 2분할 한 리스트를 각각 재귀적으로 merge_sort 
    mid = len(A) // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    
    return merge(L,R)

A = merge_sort(A)

for i in range(n):
    print(A[i])
