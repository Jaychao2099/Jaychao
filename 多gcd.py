import math
def gcd_of_multiple_numbers(*args):
    def gcd(a, b, count):
        while b != 0:
            if b > a:
                count[0] == count[0]
            else:
                count[0] += 1
            a, b = b, a % b
        return a

    if len(args) < 2:
        return "ぶ惠璶ㄢ计ㄓ璸衡程そ计"
    
    result = args[0]
    count = [0]
    for num in args[1:]:
        result = gcd(result, num, count)
    
    return result, count[0], math.floor(math.log(min(args), 2))+1


# 代刚
input_numbers = [int(x) for x in input("叫块计だ筳").split()]
result, recursion_count, floor = gcd_of_multiple_numbers(*input_numbers)
print("程そ计", result)
print("患癹Ω计", recursion_count)
print("Ω计", floor, "(度続ノ2跑计)")
