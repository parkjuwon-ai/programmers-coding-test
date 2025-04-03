def solution(numer1, denom1, numer2, denom2):
    n = numer1*denom2+numer2*denom1
    d = denom1*denom2
    
    def g(a,b):
        while b != 0:
            a, b = b, a % b
        return a
    
    gcd = g(n, d)
    return [n // gcd, d // gcd]
    
