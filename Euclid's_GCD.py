def gcd(a, b):                  #유클리드 호제법
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

a, b = input('GCD를 구하고 싶은 두 수를 입력하세요: ').split()
a = int(a)
b = int(b)

print(a, '와', b, '의 GCD값은', gcd(a,b), '입니다.')