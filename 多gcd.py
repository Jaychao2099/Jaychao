import math
def gcd_of_multiple_numbers(*args):
    def gcd(a, b, count):
        while b != 0:
            a, b = b, a % b
            count[0] += 1
        return a

    if len(args) < 2:
        return "至少需要兩個數字來計算最大公因數"
    
    result = args[0]
    count = [0]
    for num in args[1:]:
        result = gcd(result, num, count)
    
    return result, count[0], math.floor(math.log(args[1], 2))+1


# 測試
input_numbers = [int(x) for x in input("請輸入數字，以空格分隔：").split()]
result, recursion_count, floor = gcd_of_multiple_numbers(*input_numbers)
print("最大公因數：", result)
print("遞迴次數：", recursion_count)
print("次數上限：", floor, "(僅適用2個變數時。)")
