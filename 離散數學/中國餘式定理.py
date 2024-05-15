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

# 測試
input_numbers_a = [int(x) for x in input("餘數 a 為整數，模數 n 彼此互質\nx ≡ a1 (mod n1)\nx ≡ a2 (mod n2)\n  .\n  .\n  .\nx ≡ ak (mod nk)\n\n請輸入餘數a，以空格分隔：").split()]
input_numbers_n = [int(x) for x in input("請輸入模數n，以空格分隔：").split()]

# n = [3, 5, 7]
# a = [2, 3, 2]
print("n相乘 = ", total_product(input_numbers_n))
print("中國餘式定理的結果：", "x = ", chinese_remainder_theorem(input_numbers_n, input_numbers_a), "+ ", total_product(input_numbers_n), "*c", "，c 可以是任意整數。")
