def solution(n):
    root = n ** 0.5
    return int((root + 1) ** 2) if root == int(root) else -1
