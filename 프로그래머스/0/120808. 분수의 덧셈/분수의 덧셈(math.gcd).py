import math

def solution(numer1, denom1, numer2, denom2):
    n = numer1 * denom2 + numer2 * denom1
    d = denom1 * denom2
    gcd = math.gcd(n, d)
    return [n // gcd, d // gcd]
