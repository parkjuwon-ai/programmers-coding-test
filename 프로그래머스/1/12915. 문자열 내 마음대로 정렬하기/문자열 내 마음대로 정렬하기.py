def solution(strings, n):
    strings_list=[]
    answer=[]
    strings.sort()
    for i in strings:
        strings_list.append((i[n],i))
    strings_list.sort()
    for j in strings_list:
        answer.append(j[1])
    return answer