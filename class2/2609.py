# 실버 5 최대공약수와 최소공배수

def lcm(a,b):
    d = gcd(a,b)
    return d * (a//d) * (b//d)
def gcd(a,b):
    return gcd(b%a, a) if b%a else a

A,B = map(int,input().split(' '))
print(gcd(A,B) if A<B else gcd(B,A))
print(lcm(A,B) if A<B else lcm(B,A))