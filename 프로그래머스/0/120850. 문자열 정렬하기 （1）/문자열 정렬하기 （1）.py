def solution(my_string):
    num = []
    for string in my_string:
        if string.isdigit():
            num.append(int(string))
        else:
            pass
    answer = num.sort()
    answer = num
    return answer