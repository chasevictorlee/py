#辗转相除法(循环版本)
def Euclidean(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
        
    return b


print(Euclidean(123456, 7890))


#辗转相除法(递归版本)
def Euclidean2(a, b):
    if a % b == 0:
        return b
    
    return Euclidean2(b, a%b)
    

print(Euclidean2(123456, 7890))


#更相减损术(循环版本)
def reduction(a, b):
    if a <= b:
        a, b = b, a
        
    c = a - b
    while c != b:
        if b < c:
            b, c = c, b
        a = b
        b = c
        c = a - b
        
    return c

print(reduction(123456, 7890))


#更相减损术(递归版本)
def reduction2(a, b):
    if a <= b:
        a, b = b, a
        
    if a - b == b:
        return b
    
    return reduction2(b, a-b)


print(reduction2(123456, 7890))