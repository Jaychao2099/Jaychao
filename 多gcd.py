def gcd_of_multiple_numbers(*args):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if len(args) < 2:
        return "至少需要兩個數字來計算最大公因數"

    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result

# 測試
input_numbers = [int(x) for x in input("請輸入數字，以空格分隔：").split()]
print("多個數的最大公因數：", gcd_of_multiple_numbers(*input_numbers))
