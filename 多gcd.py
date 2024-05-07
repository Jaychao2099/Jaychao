def gcd_of_multiple_numbers(*args):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if len(args) < 2:
        return "�ܤֻݭn��ӼƦr�ӭp��̤j���]��"

    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result

# ����
input_numbers = [int(x) for x in input("�п�J�Ʀr�A�H�Ů���j�G").split()]
print("�h�Ӽƪ��̤j���]�ơG", gcd_of_multiple_numbers(*input_numbers))
