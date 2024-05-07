def gcd_of_multiple_numbers(*args):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if len(args) < 2:
        return "ぶ惠璶ㄢ计ㄓ璸衡程そ计"

    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result

# 代刚
input_numbers = [int(x) for x in input("叫块计だ筳").split()]
print("计程そ计", gcd_of_multiple_numbers(*input_numbers))
