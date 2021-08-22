def solution(s):
    
    index_of_substring = (s+s).find(s, 1)
    #print(f"i {i}")
    substring = s[:index_of_substring]
    #print('Substring:', sub)

    result = s.count(substring)
    print(result)

solution('abccbaabccbaabccbaabccba')
