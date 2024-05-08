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
        return "�ܤֻݭn��ӼƦr�ӭp��̤j���]��"
    
    result = args[0]
    count = [0]
    for num in args[1:]:
        result = gcd(result, num, count)
    
    return result, count[0], math.floor(math.log(min(args), 2))+1


# ����
input_numbers = [int(x) for x in input("�п�J�Ʀr�A�H�Ů���j�G").split()]
result, recursion_count, floor = gcd_of_multiple_numbers(*input_numbers)
print("�̤j���]�ơG", result)
print("���j���ơG", recursion_count)
print("���ƤW���G", floor, "(�ȾA��2���ܼƮɡC)")
