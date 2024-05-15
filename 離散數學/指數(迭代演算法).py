
num1 = int(input("base = "))
num2 = int(input("exp = "))

def power(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result

ppp = power(num1, num2)
print(f"{num1}^{num2} = {ppp}")
