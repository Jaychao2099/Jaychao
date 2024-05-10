
num1 = int(input("base = "))
num2 = int(input("exp = "))

def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return power(a, n-1) * a

ppp = power(num1, num2)
print(f"{num1}^{num2} = {ppp}")
