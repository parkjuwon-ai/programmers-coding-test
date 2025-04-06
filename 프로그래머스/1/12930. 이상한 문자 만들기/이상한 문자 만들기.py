def solution(s):

    result = ''
    index = 0  

    for ch in s:
        if ch == ' ':
            result += ' '
            index = 0
        else:
            if index % 2 == 0:
                result += ch.upper()
            else:
                result += ch.lower()
            index += 1

    return result