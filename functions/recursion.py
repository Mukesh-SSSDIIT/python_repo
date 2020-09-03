# Recursion

def sqr(m,n):
    if n == 1:
        return m
    else:
        return m * sqr(m,n-1)

ans = sqr(2,7)
print(ans)
