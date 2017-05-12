def phi(s):
    return 0.32 + s*0.33 + s*s*0.35

def go(n):
    count = 0
    s = 0
    while count < n:
        s=phi(s)
        count+=1
    return s