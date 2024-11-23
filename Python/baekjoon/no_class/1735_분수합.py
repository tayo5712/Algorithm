a,b = list(map(int,input().split(' ')))
c,d = list(map(int,input().split(' ')))

numerator = (b*c+a*d)
denominator = b*d

def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

gcd = GCD(numerator,denominator)

numerator = int(numerator/gcd)
denominator = int(denominator/gcd)

print(f"{numerator} {denominator}")