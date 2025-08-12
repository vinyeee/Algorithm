import re

def solution(s):
    
    words = re.split('( )', s)

    for j in range(len(words)):
        alphabets = list(words[j])
        for i in range(len(alphabets)):
            if i == 0 and not alphabets[i].isupper():
                alphabets[i] = alphabets[i].upper()
            elif i != 0:
                if alphabets[i].isupper():
                    alphabets[i] = alphabets[i].lower()
        words[j] = ''.join(alphabets)
        
    answer = ''.join(words)
    return answer