def solution(w,h):
    answer = w*h - getNum(w,h)
    return answer

def getNum(w, h):
    if w == h:
        return w
    gcd = GCD(max(w,h),min(w,h))
    w //= gcd
    h //= gcd
    saved = (w+h-1) * gcd
    return saved

def GCD(a,b):
    if a%b==0:
        return b
    return GCD(b,a%b)