def extended_gcd(a, b):
    """
    使用輟餘反覆相除法計算a和b的最大公因數和x,y,使得ax + by = gcd(a, b)
    返回gcd, x, y
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def chinese_remainder(n, a):
    """
    使用中國餘式定理求解同餘方程組
    n是模數的列表
    a是餘數的列表
    返回同餘方程組的解
    """
    sum = 0
    prod = 1
    for n_i in n:
        prod *= n_i
    
    for n_j, a_j in zip(n, a):
        p = prod // n_j
        g, x, y = extended_gcd(n_j, p)
        sum += a_j * x * p
    
    return sum % prod

def main():
    print("歡迎使用中國餘式定理計算機!")
    
    n = input("請輸入模數(用空格分隔): ").split()
    n = [int(x) for x in n]
    
    a = input("請輸入餘數(用空格分隔): ").split()
    a = [int(x) for x in a]
    
    if len(n) != len(a):
        print("模數和餘數的數量不相等,請重新輸入!")
        return
    
    result = chinese_remainder(n, a)
    print(f"同餘方程組的解為: {result}")

if __name__ == "__main__":
    main()