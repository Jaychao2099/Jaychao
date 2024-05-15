def A(a, b):
    while a >= 0 and b >= 0:
        if a == 0 or b <= 1:
            return 2*b
        else:
            return A(a-1, A(a, b-1))

m = int(input("請輸入第一個自然數: "))
n = int(input("請輸入第二個自然數: "))
print(f"A({m}, {n}) = {A(m, n)}")
