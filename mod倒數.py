import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def find_x(a, m):
    if gcd(a, m) != 1 or m <= 1:
        raise ValueError("Invalid input: gcd(a, m) must be 1 and m must be greater than 1")
    else:
        x_0 = modular_inverse(a, m)
        return f"x ≡ {x_0} + k*{m} (mod {m})"

# ?入 a 和 m
a = int(input("請輸入 a: "))
m = int(input("請輸入 m: "))

# ?查 gcd(a, m) 是否? 1
if gcd(a, m) != 1 or m <= 1:
    print("無效輸入: gcd(a, m) 必須為 1，且 m 必須大於 1。")
else:
    # ?算 x 的通解
    solution = find_x(a, m)
    print("x 的通解為:", solution)
