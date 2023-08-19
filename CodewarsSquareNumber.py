import math
n = 7
if n > 0:
    m = math.sqrt(n)
def is_square(n):    
    if n < 0:
        print(n," negative numbers cannot be square numbers")  
        return
    elif (m * m) == n:
        print(n," is a square number","(",m,"*",m,")")
    else:
        print(n," is not a square number")
is_square(n)