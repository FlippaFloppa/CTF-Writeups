N1=66528
N2=52920

def calc(a,b):          
    if a<b:      
        a,b = b,a #swap
    while b!=0:
        a,b = b,(a%b)
    return a

print(calc(N1,N2))
