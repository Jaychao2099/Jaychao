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
        return f"x �� {x_0} + k*{m} (mod {m})"

# ?�J a �M m
a = int(input("�п�J a: "))
m = int(input("�п�J m: "))

# ?�d gcd(a, m) �O�_? 1
if gcd(a, m) != 1 or m <= 1:
    print("�L�Ŀ�J: gcd(a, m) ������ 1�A�B m �����j�� 1�C")
else:
    # ?�� x ���q��
    solution = find_x(a, m)
    print("x ���q�Ѭ�:", solution)
