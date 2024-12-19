#정렬 해서 최대 최소 구하기 

def solution(sizes):
    answer = 0
    
    sizes = [sorted(size, reverse = True) for size in sizes ]
    
    max_width = max([size[0] for size in sizes])
    max_height = max([size[1] for size in sizes])
    
    
    return max_width * max_height