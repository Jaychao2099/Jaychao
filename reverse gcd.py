def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y



# ��J��ӼƦr
num1 = int(input("�п�J�Ĥ@�ӼƦr�G"))
num2 = int(input("�п�J�ĤG�ӼƦr�G"))

# �I�sgcd��ƨÿ�X���G
gcd, x, y = extended_euclidean(num1, num2)
print(f"gcd({num1}, {num2}) = {gcd} = {num1}*{x} + {num2}*{y}")

# print(extended_euclidean(num1, num2))

