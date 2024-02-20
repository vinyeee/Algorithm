import sys
strs = list(sys.stdin.readline().strip())

#print(strs)

def isPalindrome(strs):
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return 0
        
    return 1

print(isPalindrome(strs))