def solution(s):
    nums = []
    answer = ""
    #[-7, 1, 2, 3, 4, 5, 6]
    for i in range(len(s)):
        nums.append(ord(s[i]) - ord('a'))
    nums.sort(reverse = True)
    print(nums)
    for num in nums:
         answer += chr(num + 97)
        
    return answer