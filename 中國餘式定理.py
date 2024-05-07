def total_product(n):
    total_product = 1
    for i in n:
        total_product *= i
    return total_product

def chinese_remainder_theorem(n, a):
    total_product = 1
    for i in n:
        total_product *= i

    result = 0
    for n_i, a_i in zip(n, a):
        p = total_product // n_i
        result += a_i * mul_inv(p, n_i) * p

    return result % total_product

def mul_inv(a, b):
    b0, x0, x1 = b, 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    return x1 + b0 if x1 < 0 else x1

# 代刚
input_numbers_a = [int(x) for x in input("緇计 a ? 俱计家计 n ┘が借\nx ≥ a1 (mod n1)\nx ≥ a2 (mod n2)\n  .\n  .\n  .\nx ≥ ak (mod nk)\n\n叫块緇计aだ筳").split()]
input_numbers_n = [int(x) for x in input("叫块家计nだ筳").split()]

# n = [3, 5, 7]
# a = [2, 3, 2]
print("n = ", total_product(input_numbers_n))
print("い瓣緇Α﹚瞶挡狦", "x = ", chinese_remainder_theorem(input_numbers_n, input_numbers_a), "+ ", total_product(input_numbers_n), "*c", "c 琌ヴ種俱计")
