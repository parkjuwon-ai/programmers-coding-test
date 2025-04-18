def solution(num):
    count = 0
    while num != 1 and count < 500:
        num = num * 3 + 1 if num % 2 else num // 2
        count += 1
    return count if count < 500 else -1
