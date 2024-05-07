def decimal_to_base(decimal, base):
    if base < 2:
        return "Base must be greater than or equal to 2"
    
    digits = "0123456789ABCDEF"  # 定義16進位數字的字符集合，可根據需要擴展
    
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        remainder = decimal % base      #求餘
        result = digits[remainder] + result     
        decimal = decimal // base       #整數除法
    
    return result


# 輸入兩個數字
n = int(input("請輸入欲轉換的十進位數："))
b = int(input("請輸入進位方法："))

# 呼叫函數並輸出結果
print(n, "的", b, "進位表示法是：", decimal_to_base(n, b))

#123
