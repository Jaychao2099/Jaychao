def mod_exp(a, N, m):
    x = 1
    power = a % m
    while N > 0:
        if N % 2 == 1:
            x = (x * power) % m
        power = (power**2) % m
        N = N //2
    return x

print("求a ^ N mod m = ? (其中 N 極大)")
aa = int(input("請輸入 a: "))
NN = int(input("請輸入 N: "))
mm = int(input("請輸入 m: "))

print(f"{aa} ^ {NN} mod {mm} = {mod_exp(aa, NN, mm)}")

"""
def mod_exp(a, N, m):
    x = 1
    N = decimal_to_base(N,2)
    k = len(N)
    power = a % m
    for i in range(k-1, -1, -1):
        if N[i] == "1":
            x = (x * power) % m
        power = (power ** 2) % m
    return x


def decimal_to_base(decimal, base):
    if base < 2:
        return "Base must be greater than or equal to 2"
    
    digits = "0123456789ABCDEF"  # 定義16進位數字的字符集合，可根據需要擴展
    
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        remainder = decimal % base      #求餘
        result = digits[remainder] + result     
        decimal = decimal // base       #整數除法
    
    return result
"""