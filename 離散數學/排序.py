def sort(L: list):
    if len(L) > 1:
        m = len(L) // 2
        L = merge(sort(L[:m]), sort(L[m:]))
    return L

def merge(A, B: list):
    LL, i, j = [], 0, 0
    while i < len(A) or j < len(B):
        if i == len(A):
            LL.append(B[j])
            j += 1
        elif j == len(B):
            LL.append(A[i])
            i += 1
        elif A[i] < B[j]:
            LL.append(A[i])
            i += 1
        else:
            LL.append(B[j])
            j += 1
    return LL

input_str = input("請輸入需排序的數字，以空格分隔：")
numbers = [int(num) for num in input_str.split()]
print("排序後的數組 = ", sort(numbers))

