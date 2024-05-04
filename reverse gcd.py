def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y



# 輸入兩個數字
num1 = int(input("請輸入第一個數字："))
num2 = int(input("請輸入第二個數字："))

# 呼叫gcd函數並輸出結果
print(extended_euclidean(num1, num2))
