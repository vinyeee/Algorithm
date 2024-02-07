scale = list(map(int, input().strip().split()))

sorted_scale = sorted(scale) #오름 차순 정렬 사본 
reverse_sorted_scale = sorted(scale, reverse = True)
#print(sorted_scale)


if (sorted_scale == scale): # 오름 차순 정렬했을 때 원본과 같다면 ascending
    print("ascending")
elif(reverse_sorted_scale == scale):
    print("descending")
else :
    print("mixed")

