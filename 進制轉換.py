def decimal_to_base(decimal, base):
    if base < 2:
        return "Base must be greater than or equal to 2"
    
    digits = "0123456789ABCDEF"  # �w�q16�i��Ʀr���r�Ŷ��X�A�i�ھڻݭn�X�i
    
    if decimal == 0:
        return "0"
    
    result = ""
    while decimal > 0:
        remainder = decimal % base      #�D�l
        result = digits[remainder] + result     
        decimal = decimal // base       #��ư��k
    
    return result


# ��J��ӼƦr
n = int(input("�п�J���ഫ���̶i��ơG"))
b = int(input("�п�J�i���k�G"))

# �I�s��ƨÿ�X���G
print(n, "��", b, "�i���ܪk�O�G", decimal_to_base(n, b))

#123
